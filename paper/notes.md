# Reading notes (days 1–2)

Feeds section 2 of `report.md`. Eight papers: RAG, a RAG survey, table question answering, row-to-text serialization, retrieval over large tables, and code tools. Notes below follow the abstracts and main claims of those papers.

## Question and hypothesis

**Question.** Can RAG answer numeric questions about statistical datasets correctly, and how does the way we store the data change the result?

**Hypothesis.** Turning rows into sentences helps simple lookups. Every RAG setup fails on questions that need many rows, such as an average. A code tool, which writes pandas and runs it on the CSV, wins there.

A no-retrieval run stays in the comparison. It measures what the model already remembers. Storage C (metadata only, no numbers) is the check for made-up figures.

## What the papers show

**RAG works when the fact sits in a retrieved passage.** Lewis et al. (2020) define RAG as a generator plus a dense index of Wikipedia passages. On open-domain question answering it beats a generator that uses only its parameters, and its answers are more factual. The indexed text is prose, not a table of numbers. Gao et al. (2023) group later systems into naive RAG (retrieve, then generate), advanced RAG (rewrite the query, then rerank), and modular RAG. They treat hallucination, stale knowledge, and answers you cannot trace as the reason to retrieve. Our BM25, dense, hybrid, and hybrid-plus-reranker runs are the naive and advanced setups from that survey. Our no-retrieval run is the parametric-only baseline from Lewis et al.

**Table questions often need an operation, not a passage.** Pasupat and Liang (2015) release WikiTableQuestions: 22,033 questions on 2,108 Wikipedia tables. Questions ask for filters, comparisons, superlatives, counts, and averages. Their semantic parser, which builds a query and executes it, reaches 37.1% test accuracy and beats an information-retrieval baseline. The paper's own account is that lookup can be solved by matching surface text, and aggregation cannot.

**A row written as a sentence is a known input format, for a different task.** Hegselmann et al. (2023) turn each table row into text before prompting a language model. A simple template ("The column is value.") is one of the serializations they test, and the plain text serialization is the strongest in their released experiments. The task is few-shot classification of one row, not search over a country-by-year CSV. Storage B in this project is that serialization, moved into a retriever.

**Retrieving pieces of a numeric table is its own problem.** Chen et al. (2024) build TableRAG because program-aided models still read the whole table, which breaks on context length and on position in a long prompt. They report that embedding a long numeric row or column in one vector blurs the values. Their "read schema" baseline keeps column names and drops the cells, so the numbers are gone. That baseline is the same idea as storage C. Their retriever returns schema and cells, then a program still computes the answer. They do not test whether retrieved row text alone is enough for a single-cell lookup versus a multi-year average.

**Code fixes the arithmetic.** Gao et al. (2023, PAL) and Chen et al. (2023, Program of Thoughts) have the model write a program and a Python interpreter run it. Both find that the model can lay out the steps and still miscalculate; moving the arithmetic out of the model raises accuracy (PAL reports about 15 points over chain-of-thought on GSM8K; Program of Thoughts reports about 12 points on average across its math and financial sets). Cheng et al. (2023, Binder) take this onto tables: the model writes SQL or Python, including calls back to the model where the language is not enough, and the program executes. With a few examples and no fine-tuning, Binder is state of the art on WikiTableQuestions and TabFact, where earlier systems were trained on tens of thousands of examples. Our pandas code tool is this baseline, on a statistical CSV.

## Conclusion for this project

The hypothesis matches the split in these papers. Sentence rows (storage B) are a fair bet for one-row lookups, because language models and dense retrievers were trained on prose, and TabLLM shows that this text form is a usable encoding of a row. Lookups should be where retrieval can win over no retrieval, as in the original RAG result, provided the right row is in the top k.

Averages, trends, and other many-row questions are where retrieval is a weak fit. WikiTableQuestions already needed executed queries for those operations. A top-k list of row chunks does not contain every year in a range, and TableRAG's embedding result says a numeric row packed into one vector is a bad carrier of the figures. Storage C should produce made-up numbers whenever the model answers with a figure, because the cells were never stored. That is the same information loss as their read-schema baseline.

The code tool should win on many-row questions if the model can write the pandas. PAL, Program of Thoughts, and Binder all point that way: the model chooses the operation, and the runtime does the sum. Those papers do not run the comparison this repo runs. They do not cross three storage formats with BM25, dense search, hybrid search, and a reranker, on one statistical table, with gold answers computed from the CSV, a 1% tolerance, a made-up-number count, and a refusal check. That grid is the gap.

## References

Chen, S.-A., Miculicich, L., Eisenschlos, J. M., Wang, Z., Wang, Z., Chen, Y., Fujii, Y., Lin, H.-T., Lee, C.-Y., & Pfister, T. (2024). *TableRAG: Million-token table understanding with language models.* NeurIPS. https://arxiv.org/abs/2410.04739

Chen, W., Ma, X., Wang, X., & Cohen, W. W. (2023). *Program of Thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.* Transactions on Machine Learning Research. https://arxiv.org/abs/2211.12588

Cheng, Z., Xie, T., Shi, P., Li, C., Nadkarni, R., Hu, Y., Xiong, C., Radev, D., Ostendorf, M., Zettlemoyer, L., Smith, N. A., & Yu, T. (2023). *Binding language models in symbolic languages.* ICLR. https://arxiv.org/abs/2210.02875

Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., & Neubig, G. (2023). *PAL: Program-aided language models.* ICML. https://arxiv.org/abs/2211.10435

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M., & Wang, H. (2023). *Retrieval-augmented generation for large language models: A survey.* arXiv:2312.10997. https://arxiv.org/abs/2312.10997

Hegselmann, S., Buendia, A., Lang, H., Agrawal, M., Jiang, X., & Sontag, D. (2023). *TabLLM: Few-shot classification of tabular data with large language models.* AISTATS. https://arxiv.org/abs/2210.10723

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-augmented generation for knowledge-intensive NLP tasks.* NeurIPS. https://arxiv.org/abs/2005.11401

Pasupat, P., & Liang, P. (2015). *Compositional semantic parsing on semi-structured tables.* ACL. https://arxiv.org/abs/1508.00305

*These notes were drafted with AI assistance. Each claim is tied to the paper linked above. Open the PDF before quoting a number in `report.md`.*
