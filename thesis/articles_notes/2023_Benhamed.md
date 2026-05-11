---
id: 2023_Benhamed
title: "On the Determinants of Bitcoin Returns and Volatility: What We Get from Gets?"
citation_short: "Benhamed A., Messai A.S., El Montasser G. (2023)"
group: sentiment
pdf: "../../.local/articles/2023_Benhamed_btc_gets_method.pdf"
core: false
---

# Benhamed, Messai, El Montasser (2023) — Gets-метод для детерминант BTC

**PDF:** [`.local/articles/2023_Benhamed_btc_gets_method.pdf`](../../.local/articles/2023_Benhamed_btc_gets_method.pdf)
**Источник:** Sustainability, 15(3), 1761, 2023. DOI: 10.3390/su15031761
**Тематическая группа:** `sentiment`

## Тип работы

Эмпирическая; Gets (General-to-Specific) reduction для отбора детерминант.

## Вопрос исследования

Какой минимальный набор переменных объясняет доходность и волатильность BTC при использовании Gets-метода (от общего к частному)?

## Метод

– Gets (General-to-Specific modelling) — статистическая редукция с контролем location shifts (структурных сдвигов).
– Зависимые переменные: доходность BTC и волатильность BTC (разные модели).
– Широкий набор регрессоров: Twitter uncertainty, золото, EUR/USD, NASDAQ, капитализация, сложность майнинга, объём и др.

## Ключевые результаты

**Детерминанты доходности BTC:**
– Twitter-based economic uncertainty, доходность золота, EUR/USD, NASDAQ, капитализация BTC, mining difficulty.

**Детерминанты волатильности BTC:**
– Только лаги ARCH-эффекта и объём торгов BTC.

## Цитата для главы 1

> «The reduced set of explanatory variables that affects Bitcoin returns is composed of Twitter-based economic uncertainty, gold return, the return of the Euro/USD exchange rate, the return of the US Nasdaq stock exchange index, market capitalization, and Bitcoin mining difficulty.»

## Связь с нашей работой

– NASDAQ (≈ r_sp500) и EUR/USD (≈ r_dxy) — внешние факторы из нашей модели → Gets-метод их подтверждает.
– Объём BTC (наш `log_volume_btc`) значим для волатильности.
– Mining difficulty — ненаблюдаемый внутренний фактор, которого у нас нет, но это обосновывает ограничение нашего набора переменных.
