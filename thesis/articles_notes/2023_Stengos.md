---
id: 2023_Stengos
title: "A Bayesian approach for the determinants of bitcoin returns"
citation_short: "Stengos T., Panagiotidis T., Papapanagiotou G. (2023)"
group: volatility
pdf: "../../.local/articles/2023_Stengos_bayesian_btc_returns.pdf"
core: false
---

# Stengos, Panagiotidis, Papapanagiotou (2023) — Bayesian LASSO для доходности BTC

**PDF:** [`.local/articles/2023_Stengos_bayesian_btc_returns.pdf`](../../.local/articles/2023_Stengos_bayesian_btc_volatility.pdf)
**Источник:** Discussion Paper 2023-02, University of Guelph.
**Тематическая группа:** `volatility`

## Тип работы

Эмпирическая; отбор переменных методами байесовской регуляризации.

## Вопрос исследования

Из 31 переменной четырёх групп (финансовые, технологические, неопределённость, внимание) — какие определяют доходность BTC на периоде 2015–2021?

## Метод

– Байесовская LASSO модель со стохастической волатильностью и эффектом левериджа.
– 31 переменная: рыночные доходности, волатильности, технологические факторы (хэшрейт, сложность майнинга), индексы CBDC-неопределённости, внимание (Wikipedia, Google, Twitter).
– Ежедневные данные, 2015–2021.

## Ключевые результаты

– Сентимент и технологические факторы оказывают наибольшее влияние на доходность BTC.
– Из финансовых/экономических переменных: доходность фондового рынка и индексы волатильности (VIX) — наибольший эффект.
– CBDC-индексы неопределённости/внимания также значимы.
– Байесовский LASSO превосходит частотный LASSO в устранении смещения при отборе переменных.

## Цитата для главы 1

> «Sentiment and technological factors have the most profound effect on bitcoin returns. Regarding economic/financial variables, stock market returns and volatility indices have the greatest impact.»

## Связь с нашей работой

– Подтверждает значимость **сентимента** (Google Trends — наша переменная) и **фондового рынка** (r_sp500 — наша переменная).
– Поддерживает оба гипотетических блока: крипто-специфические (технологические, внимание) и внешние (S&P 500, VIX).
– Методологическое сравнение: мы используем OLS+Newey-West; авторы — байесовский LASSO. Сходимость результатов усиливает доверие к выводам.
