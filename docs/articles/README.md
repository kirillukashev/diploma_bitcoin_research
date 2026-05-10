# docs/articles — реестр научных статей

Публичный список статей, на которые опирается обзор литературы ВКР.
**Сами PDF в репо не заливаются** (копирайт издателей) — они лежат
локально в `.local/articles/`. Конспекты по каждой статье ведутся в
`thesis/articles_notes/<id>.md` (тоже публично, авторский текст).

– Уникальных статей: **18** (две дублирующиеся копии удалены).
– По требованиям ВКР минимум **10** научных статей; ниже из 18
  отбирается ≥10 для основного списка литературы.

## A. Классические работы

| ID | Источник |
| --- | --- |
| `2014_Glaser` | Glaser F., Zimmermann K., Haferkorn M., Weber M.C., Siering M. *Bitcoin: Asset or Currency? Revealing Users’ Hidden Intentions*. ECIS 2014, Tel Aviv. |
| `2017_Baur` | Baur D.G., Hong K., Lee A.D. *Bitcoin: Medium of Exchange or Speculative Assets?* Working Paper, UWA Business School, 2017. |
| `2018_Liu_Tsyvinski` | Liu Y., Tsyvinski A. *Risks and Returns of Cryptocurrency*. NBER WP No. 24877, 2018. (опубл.: *Review of Financial Studies*, 34(6), 2021. P. 2689–2727. DOI: 10.1093/rfs/hhaa113) |

## B. Российские исследования

| ID | Источник |
| --- | --- |
| `2021_Shilov_Zubarev` | Шилов К.Д., Зубарев А.В. *Эволюция криптовалюты биткоин как финансового актива*. Финансы: Теория и практика, Т. 25, № 5, 2021. С. 150–171. DOI: 10.26794/2587-5671-2021-25-5-150-171 |
| `2024_Sinelnikova` | Синельникова-Мурылева Е.В., Кузнецова М.Н., Шилов К.Д. *Факторные модели доходности криптовалют: подход финансовой теории*. РАНХиГС, 2024. |
| `2025_Teterin` | Тетерин М.А., Пересецкий А.А. *Can Ethereum predict Bitcoin’s volatility?* Прикладная эконометрика, Т. 77, 2025. С. 74–90. DOI: 10.22394/1993-7601-2025-77-74-90 |

## C. Волатильность и эконометрика крипты

| ID | Источник |
| --- | --- |
| `2022_Wang` | Wang J., Bouri E., Ma F., Guo Y. *Which factors drive Bitcoin volatility: macroeconomic, technical, or both?* SSRN WP, 2022. |
| `2023_Stengos` | Stengos T., Panagiotidis T., Papapanagiotou G. *A Bayesian approach for the determinants of bitcoin returns*. Discussion Paper 2023-02, University of Guelph, 2023. |
| `2024_Kufo` | Kufo A., Gjeci A., Pilkati A. *Unveiling the Influencing Factors of Cryptocurrency Return Volatility*. JRFM, 17(1), 12, 2024. DOI: 10.3390/jrfm17010012 |
| `2025_Veloso` | Veloso V., Gatsios R.C., Magnani V.M., Lima F.G. *Is Bitcoin’s Market Maturing? Cumulative Abnormal Returns and Volatility in the 2024 Halving and Past Cycles*. JRFM, 18(5), 242, 2025. DOI: 10.3390/jrfm18050242 |

## D. Макроэкономические факторы

| ID | Источник |
| --- | --- |
| `2024_Tzeng` | Tzeng K.-Y., Su Y.-K. *Can U.S. macroeconomic indicators forecast cryptocurrency volatility?* North American Journal of Economics and Finance, Vol. 74, 2024. P. 102224. DOI: 10.1016/j.najef.2024.102224 |
| `2024_Wahyuni` | Wahyuni M.T., Ridwan E., Salim D.F. *US macroeconomic determinants of Bitcoin*. Investment Management and Financial Innovations, 21(2), 2024. P. 240–252. DOI: 10.21511/imfi.21(2).2024.19 |
| `2025_Lin` | Lin M., Liu Y., Sheng V.N.K. *Analysis of the impact of macroeconomic factors on cryptocurrency returns – Based on quantile regression study*. International Review of Economics and Finance, Vol. 97, 2025. P. 103757. DOI: 10.1016/j.iref.2024.103757 |
| `2025_Pourpourides` | Pourpourides P.M. *Long-term nexus of macroeconomic and financial fundamentals with cryptocurrencies*. Frontiers in Blockchain, Vol. 8, 2025. Article 1550720. |

## E. Сентимент, новости, рыночные ожидания

| ID | Источник |
| --- | --- |
| `2023_Benhamed` | Benhamed A., Messai A.S., El Montasser G. *On the Determinants of Bitcoin Returns and Volatility: What We Get from Gets?* Sustainability, 15(3), 1761, 2023. DOI: 10.3390/su15031761 |
| `2024_Mohanty` | Mohanty H., Krishnamachari B. *Do Prediction Markets Forecast Cryptocurrency Volatility? Evidence from Kalshi Macro Contracts*. Working Paper, USC Viterbi, 2024. |

## F. Систематические обзоры и survey-работы

| ID | Источник |
| --- | --- |
| `2024_Peng` | Peng S., Prentice C., Shams S., Sarker T. *A systematic literature review on the determinants of cryptocurrency pricing*. China Accounting and Finance Review, 2024. |
| `2025_Kang` | Kang D., Ryu D., Webb R.I. *Bitcoin as a financial asset: a survey*. Financial Innovation, Vol. 11, 2025. Article 101. DOI: 10.1186/s40854-025-00773-0 |

## Что делать дальше

1. Прочитать каждую статью и заполнить конспект в
   `thesis/articles_notes/<id>.md` (поля «Метод», «Результаты», «Цитата
   для главы 1», «Связь с нашей работой»).
2. Отобрать ≥10 статей для основного списка литературы — пометить
   `core: true` в YAML-шапке конспекта.
3. Перенести метаданные отобранных статей в `thesis/references.md` по
   ГОСТ 7.1.
