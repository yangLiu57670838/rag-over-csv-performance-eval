# RAG over Statistical Data – Project Plan

**Repo:** `rag-statqa`
**Time:** 2 weeks
**Output:** a public GitHub repo + a research report in `report.md` (4–6 pages)

---

## 1. Goal

Find out if RAG can answer number questions about data tables, and which way of storing the data works best.

## 2. Research question

> Can RAG answer numeric questions about statistical datasets correctly, and how does the way we store the data change the result?

**Hypothesis:** turning rows into sentences helps with simple lookups, but all RAG setups fail on questions that need many rows (like averages). A code tool wins there.

## 3. Data

| Dataset | Shape | Use |
|---|---|---|
| [OWID CO₂ data](https://github.com/owid/co2-data) | country × year | main dataset |
| OWID notable AI models | one row per model | different shape, recent values |
| [OWID energy data](https://github.com/owid/energy-data) (optional) | country × year | extra check |

Rules:
- Keep about 8 columns and years from 1990 on. Small tables give cleaner tests.
- Pick less famous columns (e.g. methane per person), so the model can't answer from memory.
- Save the download date and version in `data/README.md`.

## 4. What we compare

**How the data is stored (3 ways):**

| ID | Storage | Example |
|---|---|---|
| A | Raw rows | `country,year,co2_per_capita` / `Australia,2020,15.4` |
| B | Rows as sentences | "In 2020, Australia's CO₂ per person was 15.4 tonnes." |
| C | Metadata only (control) | "This dataset has CO₂ data by country and year…" |

**How we search:**
- BM25 (keyword search)
- dense search (embeddings)
- hybrid (both)
- hybrid + reranker

**Baselines:**
- **No retrieval:** the LLM answers alone. This shows what it already remembers.
- **Code tool:** the LLM writes pandas code and runs it on the CSV. This is the strong baseline.

**Models:** one API model and one small local model (via Ollama).

## 5. Questions (the benchmark)

- Make 300+ questions from templates, e.g. "What was {column} of {country} in {year}?".
- Get the right answer with pandas from the CSV. No hand checking needed.
- Rewrite about 20% of the questions by hand, so they don't all sound the same.
- Save them in `eval/questions.jsonl`, with fields `id, type, question, answer, dataset, rows_needed`.

| Type | Example | Rows needed |
|---|---|---|
| Lookup | CO₂ per person of Australia in 2020? | 1 |
| Compare | Did Japan or Germany emit more in 2015? | 2 |
| Trend | Did France's emissions go up or down since 1990? | 2+ |
| Aggregate | Average emissions of India, 2000–2020? | many |
| Unanswerable | CO₂ of Australia in 1850? (not in data) | 0 |

## 6. Metrics

- **Accuracy:** an answer is right if it is within 1% of the true number. Yes/no questions use exact match.
- **Recall@k:** did search find the right rows?
- **Made-up numbers:** the model gives a number when the right rows were not found, or in setup C.
- **Refusal:** does it say "I don't know" for unanswerable questions?
- **Cost and speed:** tokens and seconds per question.

## 7. Repo layout

```
rag-statqa/
├── README.md            # question, main results table, how to run
├── prd.md               # this file
├── configs/             # one YAML per experiment
├── data/                # download script + data README (no big files)
├── src/
│   ├── ingest.py        # load data, make chunks (A / B / C)
│   ├── make_questions.py# build questions + answers from CSV
│   ├── retrieve.py      # BM25, dense, hybrid, rerank
│   ├── generate.py      # prompt + LLM call
│   ├── code_tool.py     # pandas baseline
│   └── evaluate.py      # metrics
├── eval/questions.jsonl
├── results/             # CSVs + charts per run
├── paper/               # reading notes (input to the report)
├── report.md            # research report (the written result)
└── run.py               # python run.py --config configs/xxx.yaml
```

**Tools:** Python, pandas, `rank_bm25`, `sentence-transformers` (BGE), FAISS, a BGE reranker, Ollama.

**Rule:** build the pipeline yourself first. Don't use LangChain or LlamaIndex, so you learn how each part works.

## 8. Plan (14 days)

| Day | Task | Done when |
|---|---|---|
| 1–2 | Read 5–8 papers (RAG, table QA, RAG survey). Write the question and hypothesis. | 1-page notes in `paper/notes.md` |
| 3 | Download data, cut columns and years, set up the repo | data loads in one script |
| 4–5 | Build the questions + answers from the CSV | 300+ questions, all 5 types |
| 6–7 | Build ingest (A/B/C), search, and LLM call | one question runs end to end |
| 8 | Add the baselines: no retrieval + code tool | all setups run |
| 9 | Run all experiments, fix seeds, save configs | full results table |
| 10 | Read 30–50 wrong answers by hand and group them by cause | error types with examples |
| 11–13 | Write the research report in `report.md` and make 2–3 charts | full draft, every number taken from `results/` |
| 14 | Clean the README, link the report, test a fresh run, publish | one command reproduces the results |

## 9. Research report plan

The written result is `report.md` (about 4–6 pages). Reading notes stay in `paper/notes.md` and feed section 2. Charts are made from `results/` and placed in the report.

**When:** days 11–13, after the full results table (day 9) and the hand read of wrong answers (day 10). Day 14 links `report.md` from the README.

**Rules:**
- Every number comes from `results/`. Do not fill in scores before the runs exist.
- Open with the research question and three findings a reader can check in the tables.
- Break results down by question type (lookup, compare, trend, aggregate, unanswerable). An overall average hides where RAG fails.
- In the error section, quote real wrong answers and name the cause.
- Close with a short note on where AI was used.

| Section | Write this | Take it from |
|---|---|---|
| 1. Intro | The problem, the research question, the hypothesis, and 3 main findings | Section 2 of this file, plus the results table |
| 2. Related work | RAG, table QA, and text-to-SQL / code tools (~10 papers) | `paper/notes.md` |
| 3. Setup | Datasets, how questions were built, storage A/B/C, search methods, baselines, models, metrics | Sections 3–6 of this file |
| 4. Results | One main table of all setups × question types, plus 2–3 charts | `results/` |
| 5. Error analysis | 30–50 wrong answers grouped by cause, each group with an example | Day-10 notes and run logs |
| 6. Limits | Small benchmark, few datasets, many template questions | What was actually run |
| 7. Conclusion | What the comparison showed, and what it does not show | Sections 4 and 5 |
| AI use | What was written or coded with AI assistance | This project |

## 10. Risks

| Risk | Fix |
|---|---|
| API cost too high | test on 50 questions first; use the local model for most runs |
| Model knows answers from memory | use less famous columns; report the no-retrieval score |
| Row chunks too long | fewer columns; repeat the header only once per chunk |
| Not enough time | drop the energy dataset and the reranker first |

## 11. Done means

- [ ] One command reproduces all results
- [ ] Questions + answers are public in the repo
- [ ] The results table covers all setups and question types
- [ ] The error analysis has real examples
- [ ] The research report (`report.md`) is finished and linked in the README
- [ ] AI use is noted in the README and the report
