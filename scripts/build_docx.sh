#!/usr/bin/env bash
# Сборка ВКР в docx через pandoc по требованиям методички РАНХиГС 2023.
#
# Использование (из корня репозитория):
#   bash scripts/build_docx.sh
#
# На выходе:
#   thesis_vkr.docx — основной текст ВКР (Введение, Главы 1-3, Заключение,
#   Список литературы) со стилями, соответствующими §2.2.4–§2.2.10
#   методических рекомендаций.
#
# Логика:
# 1. Подготовить scripts/reference.docx (один раз, через
#    python3 scripts/customize_reference.py) — задаёт поля 35/10/15/15 мм,
#    Times New Roman 12 pt (14 для глав), интервал 1.5, абзацный отступ 1.25 см.
# 2. Скопировать markdown во временную директорию и заменить
#    \tag{N.N} → \qquad (N.N) для корректной конвертации формул.
# 3. Запустить pandoc с --reference-doc=scripts/reference.docx.
# 4. Постобработка через python3 scripts/postprocess_docx.py — центрирует
#    подписи таблиц/рисунков, добавляет нумерацию страниц.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT/thesis"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

REF_DOC="$ROOT/scripts/reference.docx"
if [ ! -f "$REF_DOC" ]; then
  echo "reference.docx не найден, генерирую заново..."
  pandoc -o "$REF_DOC" --print-default-data-file reference.docx
fi
python3 "$ROOT/scripts/customize_reference.py"

FILES=(
  "01_introduction.md"
  "02_chapter1_literature.md"
  "03_chapter2_methodology.md"
  "04_chapter3_results.md"
  "05_conclusion.md"
  "references.md"
)

for f in "${FILES[@]}"; do
  perl -pe 's/\\tag\{([^}]+)\}/\\qquad ($1)/g' "$SRC_DIR/$f" > "$TMP_DIR/$f"
done

OUT="$ROOT/thesis_vkr.docx"

cd "$TMP_DIR"
pandoc \
  "${FILES[@]}" \
  -o "$OUT" \
  --reference-doc="$REF_DOC" \
  --resource-path="$SRC_DIR" \
  --resource-path="$ROOT" \
  -f markdown+tex_math_dollars \
  -t docx

python3 "$ROOT/scripts/postprocess_docx.py" "$OUT"

echo "Готово: $OUT"
