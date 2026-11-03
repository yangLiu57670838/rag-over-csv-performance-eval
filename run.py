# Purpose: one entry point for an experiment.
# Usage: python run.py --config configs/<name>.yaml
#
# Reads the YAML, then runs the RAG steps in order. Search steps are
# alternatives picked by the config, not steps that all run every time.
#
# Offline (once per dataset + storage mode):
#   data/download.py
#   src/rag/01_load_data.py
#   src/make_questions.py          # benchmark, not part of answering
#   src/rag/02_make_chunks.py      # storage A, B, or C
#   src/rag/03_build_bm25_index.py # when search is bm25 or hybrid
#   src/rag/04_embed_chunks.py     # when search is dense or hybrid
#   src/rag/05_build_faiss_index.py
#
# Online (once per question):
#   src/rag/06_search_bm25.py      # or 07 dense, or 08 hybrid
#   src/rag/09_rerank.py           # only when the config asks for a reranker
#   src/rag/10_generate.py
#   — or, instead of search + generate —
#   src/rag/11_baseline_no_retrieval.py
#   src/rag/12_baseline_code_tool.py
#
# After the run:
#   src/rag/13_evaluate.py         # writes into results/
