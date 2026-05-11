"""Настраивает scripts/reference.docx под требования РАНХиГС (методичка 2023).

Параметры страницы:
- A4, поля: левое 35 мм, правое 10 мм, верхнее/нижнее 15 мм
- Шрифт: Times New Roman, 12 pt — основной, 14 pt — заголовки глав
- Интервал 1.5
- Абзацный отступ первой строки: 1.25 см
- Основной текст по ширине, заголовки слева
- Подписи таблиц и рисунков по центру
"""

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.shared import Cm, Mm, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


REF = Path(__file__).resolve().parent / "reference.docx"


def set_run_font(run_props, font_name="Times New Roman", size_pt=12, bold=False):
    if run_props is None:
        return
    rfonts = run_props.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        run_props.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), font_name)

    sz = run_props.find(qn("w:sz"))
    if sz is None:
        sz = OxmlElement("w:sz")
        run_props.append(sz)
    sz.set(qn("w:val"), str(size_pt * 2))

    sz_cs = run_props.find(qn("w:szCs"))
    if sz_cs is None:
        sz_cs = OxmlElement("w:szCs")
        run_props.append(sz_cs)
    sz_cs.set(qn("w:val"), str(size_pt * 2))

    b = run_props.find(qn("w:b"))
    if bold:
        if b is None:
            b = OxmlElement("w:b")
            run_props.append(b)
        b.set(qn("w:val"), "true")
    else:
        if b is not None:
            b.set(qn("w:val"), "false")


def set_paragraph_format(
    para_props,
    alignment="both",
    first_line_cm=1.25,
    line_spacing=1.5,
    space_before=0,
    space_after=0,
    keep_with_next=False,
):
    if para_props is None:
        return

    jc = para_props.find(qn("w:jc"))
    if jc is None:
        jc = OxmlElement("w:jc")
        para_props.append(jc)
    jc.set(qn("w:val"), alignment)

    ind = para_props.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        para_props.append(ind)
    if first_line_cm and first_line_cm > 0:
        ind.set(qn("w:firstLine"), str(int(first_line_cm * 567)))
        if qn("w:left") in ind.attrib:
            del ind.attrib[qn("w:left")]
    else:
        for a in ("w:firstLine", "w:left", "w:hanging"):
            if qn(a) in ind.attrib:
                del ind.attrib[qn(a)]

    spacing = para_props.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        para_props.append(spacing)
    spacing.set(qn("w:before"), str(int(space_before * 20)))
    spacing.set(qn("w:after"), str(int(space_after * 20)))
    spacing.set(qn("w:line"), str(int(line_spacing * 240)))
    spacing.set(qn("w:lineRule"), "auto")

    if keep_with_next:
        kwn = para_props.find(qn("w:keepNext"))
        if kwn is None:
            kwn = OxmlElement("w:keepNext")
            para_props.append(kwn)


def get_or_create_style_props(style):
    elem = style.element
    pPr = elem.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        elem.append(pPr)
    rPr = elem.find(qn("w:rPr"))
    if rPr is None:
        rPr = OxmlElement("w:rPr")
        elem.append(rPr)
    return pPr, rPr


def configure_styles(doc):
    styles = doc.styles

    pPr, rPr = get_or_create_style_props(styles["Normal"])
    set_run_font(rPr, size_pt=12, bold=False)
    set_paragraph_format(pPr, alignment="both", first_line_cm=1.25, line_spacing=1.5)

    heading_specs = {
        "Heading 1": {"size": 14, "before": 18, "after": 12, "first_line": 0, "align": "left"},
        "Heading 2": {"size": 12, "before": 12, "after": 6, "first_line": 0, "align": "left"},
        "Heading 3": {"size": 12, "before": 6, "after": 6, "first_line": 0, "align": "left"},
        "Heading 4": {"size": 12, "before": 6, "after": 6, "first_line": 0, "align": "left"},
    }
    for name, spec in heading_specs.items():
        if name not in styles:
            continue
        pPr, rPr = get_or_create_style_props(styles[name])
        set_run_font(rPr, size_pt=spec["size"], bold=True)
        set_paragraph_format(
            pPr,
            alignment=spec["align"],
            first_line_cm=spec["first_line"],
            line_spacing=1.5,
            space_before=spec["before"],
            space_after=spec["after"],
            keep_with_next=True,
        )

    if "Title" in styles:
        pPr, rPr = get_or_create_style_props(styles["Title"])
        set_run_font(rPr, size_pt=14, bold=True)
        set_paragraph_format(
            pPr,
            alignment="center",
            first_line_cm=0,
            line_spacing=1.5,
            space_before=0,
            space_after=24,
        )

    for caption_name in ("Image Caption", "Caption", "Table Caption"):
        if caption_name in styles:
            pPr, rPr = get_or_create_style_props(styles[caption_name])
            set_run_font(rPr, size_pt=12, bold=False)
            set_paragraph_format(
                pPr,
                alignment="center",
                first_line_cm=0,
                line_spacing=1.5,
                space_before=6,
                space_after=12,
            )

    if "Compact" in styles:
        pPr, rPr = get_or_create_style_props(styles["Compact"])
        set_run_font(rPr, size_pt=12, bold=False)
        set_paragraph_format(pPr, alignment="both", first_line_cm=0, line_spacing=1.5)

    for list_name in ("List Paragraph", "Bullet List", "Numbered List"):
        if list_name in styles:
            pPr, rPr = get_or_create_style_props(styles[list_name])
            set_run_font(rPr, size_pt=12, bold=False)
            set_paragraph_format(pPr, alignment="both", first_line_cm=0, line_spacing=1.5)


def configure_section(doc):
    section = doc.sections[0]
    section.page_height = Mm(297)
    section.page_width = Mm(210)
    section.left_margin = Mm(35)
    section.right_margin = Mm(10)
    section.top_margin = Mm(15)
    section.bottom_margin = Mm(15)
    section.header_distance = Mm(7)
    section.footer_distance = Mm(7)


def main():
    doc = Document(str(REF))
    configure_styles(doc)
    configure_section(doc)
    doc.save(str(REF))
    print(f"reference.docx обновлён: {REF}")


if __name__ == "__main__":
    main()
