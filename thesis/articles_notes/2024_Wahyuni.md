---
id: 2024_Wahyuni
title: "US macroeconomic determinants of Bitcoin"
citation_short: "Wahyuni M.T., Ridwan E., Salim D.F. (2024)"
group: macro
pdf: "../../.local/articles/2024_Wahyuni_us_macro_btc.pdf"
core: false
---

# Wahyuni, Ridwan, Salim (2024) — Макродетерминанты Bitcoin в США

**PDF:** [`.local/articles/2024_Wahyuni_us_macro_btc.pdf`](../../.local/articles/2024_Wahyuni_us_macro_btc.pdf)
**Источник:** Investment Management and Financial Innovations, 21(2), 2024. P. 240–252. DOI: 10.21511/imfi.21(2).2024.19
**Тематическая группа:** `macro`

## Тип работы

Эмпирическая; DCC-MGARCH для анализа динамической корреляции BTC с макропеременными.

## Вопрос исследования

Как американские макроэкономические переменные (инфляция, процентные ставки, курс USD/EUR, цена золота) влияют на цену Bitcoin?

## Метод

– Ежемесячные данные, 2017–2022.
– Dynamic Conditional Correlation (DCC) + Multivariate GARCH (MGARCH).
– Переменные: CPI (inflation), Fed funds rate, USD/EUR, gold price, bitcoin price.

## Ключевые результаты

– **Инфляция, процентные ставки и курс USD/EUR отрицательно** и значимо связаны с ценой BTC.
– **Цена золота положительно** связана с ценой BTC.
– DCC подтверждает, что корреляции не постоянны: они меняются со временем.

## Цитата для главы 1

> «There is a negative and significant relationship between the variables of inflation, interest rates, and USD/EUR rates affecting the price of Bitcoin... Conversely, there is a positive and significant relationship between the price of gold and the price of Bitcoin.»

## Связь с нашей работой

– Отрицательная связь USD с BTC → наша переменная `r_dxy` (индекс доллара): ожидаемый знак совпадает.
– Инфляция → VIX как более широкий прокси неопределённости в нашей работе.
– Поддерживает включение внешних макрофакторов в модель — обосновывает наш внешний блок.
