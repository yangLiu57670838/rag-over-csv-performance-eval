# Can RAG Answer Numeric Questions about Statistical Tables?

Research report. Plan and section rules are in `prd.md` (section 9).
About 4–6 pages. Every number below comes from `results/`. Leave a section blank until that evidence exists.

## 1. Intro

State the problem, the research question, and the hypothesis.
End with three findings a reader can check in the results table.

## 2. Related work

Cover RAG, table question answering, and text-to-SQL / code tools (about 10 papers).
Source: `paper/notes.md`.

## 3. Setup

- **Data:** OWID CO₂ (main), OWID notable AI models, optional OWID energy. Columns kept, year filter, download date and version.
- **Questions:** 300+ items in `eval/questions.jsonl`. Types: lookup, compare, trend, aggregate, unanswerable.
- **Storage:** A raw rows, B rows as sentences, C metadata only.
- **Search:** BM25, dense, hybrid, hybrid + reranker.
- **Baselines:** no retrieval, and the pandas code tool.
- **Models:** one API model and one small local model (Ollama).
- **Metrics:** accuracy (within 1%; exact match for yes/no), recall@k, made-up numbers, refusal, tokens and seconds per question.

## 4. Results

Main table: each setup by question type.
Then 2–3 charts from `results/`.
Say where storage B helps lookups, where every RAG setup fails on many-row questions, and how the code tool compares.

## 5. Error analysis

Group 30–50 wrong answers by cause. For each cause, give one real example (question, retrieved rows, model answer, gold answer).

## 6. Limits

Small benchmark, few datasets, and many questions that still follow a template.

## 7. Conclusion

What the comparison showed, and what it does not show.

## Note on AI use

Say what in this repo and this report was done with AI assistance.
