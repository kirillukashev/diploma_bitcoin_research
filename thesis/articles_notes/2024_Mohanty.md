---
id: 2024_Mohanty
title: "Do Prediction Markets Forecast Cryptocurrency Volatility? Evidence from Kalshi"
citation_short: "Mohanty H., Krishnamachari B. (2024/2026)"
group: sentiment
pdf: "../../.local/articles/2024_Mohanty_kalshi_prediction_markets.pdf"
core: false
---

# Mohanty, Krishnamachari (2026) — Prediction Markets Kalshi и волатильность крипты

**PDF:** [`.local/articles/2024_Mohanty_kalshi_prediction_markets.pdf`](../../.local/articles/2024_Mohanty_kalshi_prediction_markets.pdf)
**Источник:** Working Paper, USC Viterbi School of Engineering; arXiv:2604.01431, апрель 2026.
**Тематическая группа:** `sentiment`

## Тип работы

Эмпирическая; прогнозирование реализованной волатильности по prediction-market сигналам.

## Вопрос исследования

Содержат ли ежедневные изменения вероятностей на рынках предсказаний Kalshi информацию о будущей волатильности криптовалют (BTC, ETH, SOL и др.)?

## Метод

– Ежедневные данные по 10 Kalshi event-сериям и 6 криптовалютам, январь 2023 — март 2026.
– HAR-модели для реализованной волатильности (5-дневный горизонт прогноза).
– Три канала: монетарная политика (KXFED), риск рецессии (KXRECSSNBER), инфляция (KXCPI).
– Робастность: ортогонализация относительно Fed Funds futures, Treasury yields, Deribit IV.
– Benjamini-Hochberg коррекция на множественное тестирование.

## Ключевые результаты

– Fed-repricing (KXFED) предсказывает волатильность BTC in-sample (t=3.63, p<0.001), но нестабильно out-of-sample.
– Recession risk (KXRECSSNBER) стабильно out-of-sample: MSFE=0.979, p=0.020.
– Inflation channel (KXCPI) предсказывает волатильность альткоинов (ETH, SOL, ADA, LINK).
– BTC реагирует на монетарную политику; альткоины — на инфляцию.

## Цитата для главы 1

> «Bitcoin volatility is governed by institutional investors reacting to monetary policy expectations, and altcoin volatility by retail participants navigating inflation regime uncertainty.»

## Связь с нашей работой

– Наиболее экзотичная статья в списке, методологически далеко от нашей работы.
– Концептуально: монетарная политика (Fed) → VIX и r_sp500 как прокси в нашей работе.
– Институциональная реакция на Fed-ожидания — объяснение растущей корреляции с S&P 500 в 2020–2025.
– Можно упомянуть во введении как свидетельство зрелости крипторынка.
