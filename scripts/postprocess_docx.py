"""Постобработка thesis_vkr.docx после pandoc.

Доработки под методичку РАНХиГС 2023:
1. Нумерация страниц по центру верхнего поля (со 2-й страницы — на титуле
   номера не будет; titlePg = особый колонтитул для 1-й страницы).
2. Разрыв страницы перед каждой Heading 1, кроме первой («Введение»).
3. Подписи «Таблица N.N — ...» и «Рисунок N.N — ...» по центру, без
   абзацного отступа, без курсива.
4. Маркер «–» (en-dash) для всех ненумерованных списков (§2.2.6).
5. «Введение», «Заключение», «Список литературы», «Оглавление» —
   по центру, без абзацного отступа.
"""

import re
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


CAPTION_RE = re.compile(r"^(Таблица|Рисунок)\s+\d+(\.\d+)*\s*[—–-]")


def add_page_numbers(doc):
    section = doc.sections[0]
    header = section.header
    header.is_linked_to_previous = False
    p = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in list(p.runs):
        run.text = ""
    run = p.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)

    sectPr = section._sectPr
    titlePg = sectPr.find(qn("w:titlePg"))
    if titlePg is None:
        titlePg = OxmlElement("w:titlePg")
        sectPr.append(titlePg)


def clear_first_line_indent(para):
    pPr = para._p.get_or_add_pPr()
    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    for attr in ("w:firstLine", "w:left", "w:hanging"):
        if qn(attr) in ind.attrib:
            del ind.attrib[qn(attr)]


def add_page_break_before(para):
    pPr = para._p.get_or_add_pPr()
    pbb = pPr.find(qn("w:pageBreakBefore"))
    if pbb is None:
        pbb = OxmlElement("w:pageBreakBefore")
        pPr.append(pbb)


def add_breaks_before_headings(doc):
    first_h1_seen = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1":
            if not first_h1_seen:
                first_h1_seen = True
                continue
            add_page_break_before(para)


def center_captions(doc):
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        if CAPTION_RE.match(text):
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            clear_first_line_indent(para)
            for run in para.runs:
                run.italic = False


def fix_special_headings(doc):
    targets = {"введение", "заключение", "список литературы", "оглавление"}
    for para in doc.paragraphs:
        if not para.style or not para.style.name.startswith("Heading"):
            continue
        if para.text.strip().lower() in targets:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            clear_first_line_indent(para)


def fix_bullet_markers(docx_path: Path):
    """Меняет маркеры всех ненумерованных списков на тире (–)."""
    import shutil
    import tempfile

    with zipfile.ZipFile(docx_path) as z:
        if "word/numbering.xml" not in z.namelist():
            return
        with z.open("word/numbering.xml") as f:
            numbering = f.read().decode("utf-8")

    bullet_chars = {"\uf0b7", "\u2022", "o", "\uf0a7", "\u25aa", "\u00b7"}
    pattern = re.compile(
        r'(<w:lvlText\s+w:val=")([^"]+)("\s*/?>)'
    )

    def replace_marker(match):
        prefix, value, suffix = match.group(1), match.group(2), match.group(3)
        if value in bullet_chars:
            return f"{prefix}\u2013{suffix}"
        return match.group(0)

    new_numbering = pattern.sub(replace_marker, numbering)

    new_numbering = re.sub(
        r'(<w:numFmt\s+w:val=")bullet(")',
        r'\1bullet\2',
        new_numbering,
    )

    if new_numbering == numbering:
        return

    tmp = Path(tempfile.mkdtemp()) / "out.docx"
    with zipfile.ZipFile(docx_path, "r") as src, zipfile.ZipFile(
        tmp, "w", zipfile.ZIP_DEFLATED
    ) as dst:
        for item in src.namelist():
            if item == "word/numbering.xml":
                dst.writestr(item, new_numbering)
            else:
                dst.writestr(item, src.read(item))
    shutil.move(str(tmp), str(docx_path))


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: postprocess_docx.py <path>")
    path = Path(sys.argv[1])
    doc = Document(str(path))
    add_page_numbers(doc)
    add_breaks_before_headings(doc)
    center_captions(doc)
    fix_special_headings(doc)
    doc.save(str(path))
    fix_bullet_markers(path)
    print(f"Постобработка применена: {path}")


if __name__ == "__main__":
    main()
