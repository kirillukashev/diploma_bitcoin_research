---
id: 2025_Teterin
title: "Can Ethereum predict Bitcoin's volatility?"
citation_short: "Тетерин М.А., Пересецкий А.А. (2025)"
group: russian
pdf: "../../.local/articles/2025_Teterin_eth_predicts_btc_volatility.pdf"
core: false
---

# Тетерин, Пересецкий (2025) — Can Ethereum predict Bitcoin's volatility?

**PDF:** [`.local/articles/2025_Teterin_eth_predicts_btc_volatility.pdf`](../../.local/articles/2025_Teterin_eth_predicts_btc_volatility.pdf)
**Источник:** Прикладная эконометрика, Т. 77, 2025. С. 74–90. DOI: 10.22394/1993-7601-2025-77-74-90
**Тематическая группа:** `russian`

## Тип работы

Эмпирическая; прогнозирование реализованной волатильности.

## Вопрос исследования

Улучшает ли добавление волатильности ETH в модель прогноза точность прогноза волатильности BTC, и наоборот?

## Метод

– Высокочастотные данные BTC и ETH, 01.01.2018 — 23.06.2024.
– Реализованная волатильность (RV) с 5-минутным интервалом.
– Базовая модель: HAR-RV (Heterogeneous Autoregressive Realized Volatility).
– Расширенные модели: HAR-RV + экзогенные переменные другой крипты; VAR-HAR-RV (векторная модель).
– Rolling window, >2000 out-of-sample прогнозов; сравнение по MCS (Model Confidence Set).
– Функции потерь: MSE, QLIKE и др.

## Ключевые результаты

– Волатильность ETH значимо улучшает прогноз RV для BTC (и наоборот).
– MCS показывает, что расширенная модель превосходит базовую HAR-RV статистически значимо.
– Эффект spillover: шоки волатильности одной крипты передаются другой.
– VAR-HAR-RV дополнительно улучшает прогноз, подтверждая двустороннюю связь.

## Цитата для главы 1

> «The models which incorporate Bitcoin data show that Bitcoin's volatility significantly contributes to forecasts of Ethereum's volatility across different forecast horizons.»

## Связь с нашей работой

– Показывает тесную связь между BTC и ETH: spillover-эффекты внутри крипторынка — это внутренний крипто-специфический фактор.
– Методологически ближе к робастности нашей GARCH-модели, чем к основному анализу.
– Актуальна для обзора литературы в блоке «внутренние факторы».
