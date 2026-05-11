---
id: 2018_Liu_Tsyvinski
title: "Risks and Returns of Cryptocurrency"
citation_short: "Liu Y., Tsyvinski A. (2018; опубл. 2021)"
group: classics
pdf: "../../.local/articles/2018_Liu_Tsyvinski_crypto_risks_returns.pdf"
core: false
---

# Liu, Tsyvinski (2018; опубл. 2021) — Risks and Returns of Cryptocurrency

**PDF:** [`.local/articles/2018_Liu_Tsyvinski_crypto_risks_returns.pdf`](../../.local/articles/2018_Liu_Tsyvinski_crypto_risks_returns.pdf)
**Источник:** NBER Working Paper 24877, 2018; опубл. *The Review of Financial Studies*, 34(6), 2021. P. 2689–2727. DOI: 10.1093/rfs/hhaa113
**Тематическая группа:** `classics`

## Тип работы

Эмпирическая; стандартные инструменты эмпирического ценообразования активов применены к крипторынку.

## Вопрос исследования

Можно ли объяснить доходность криптовалют факторами фондового, валютного, товарного рынков? Какие крипто-специфические предикторы работают?

## Метод

– BTC (с 01.01.2011), XRP (с 08.04.2013), ETH (с 08.07.2015) — по 31.05.2018. Источник: CoinDesk.
– CAPM, Fama-French 3F/5F/6F, Carhart 4F — проверка нагрузок на стандартные факторы риска.
– 155 аномалий из литературы (база А. Чена).
– Time-series и cross-section регрессии. Quintile портфельная сортировка по моментуму.
– Google Trends, Twitter (Crimson Hexagon) — прокси внимания инвесторов.
– Частоты: дневные, недельные, месячные.

## Ключевые результаты

– CAPM бета значима, но альфа остаётся большой и значимой — крипта не объясняется рыночным фактором.
– Нагрузки на Fama-French факторы малы и незначимы (за исключением HML у Ripple).
– Нет значимой связи с 5 основными валютами (AUD, CAD, EUR, SGD, GBP).
– Нет значимой связи с драгоценными металлами (золото, серебро, платина).
– **Значимы крипто-специфические факторы:** time-series momentum (1 s.d. → +0.33% на следующий день), Google Trends (+1 s.d. → +2.3% за 2 недели), Twitter (+1 s.d. → +2.5% за 1 неделю).
– Price-to-"dividend" ratio (цена / число кошельков) и реализованная волатильность доходность не предсказывают.

## Цитата для главы 1

> «Cryptocurrencies have no exposure to most common stock market and macroeconomic factors... the cryptocurrency returns can be predicted by factors which are specific to cryptocurrency markets.»

## Связь с нашей работой

– **Ключевая работа для обоснования H1**: крипто-специфические факторы (объём, внимание) — естественные предикторы BTC.
– Наши факторы `google_trends` и `log_volume_btc` напрямую мотивированы этой статьёй.
– **Отличие:** данные Liu & Tsyvinski заканчиваются в 2018 г.; в нашем периоде 2020–2025 внешние факторы (S&P 500) значимее крипто-специфических → H1 в нашей работе **отвергается**, что расширяет выводы классики.
