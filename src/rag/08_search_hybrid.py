# Purpose: step 6c. Combine keyword search and vector search.
#
# Input:  results from 06_search_bm25.py and 07_search_dense.py
#         for the same question.
# Output: one merged top-k list (both hit lists, scores combined).
#
# Run it when the config says search: hybrid or hybrid_rerank.
# Next: 09_rerank.py if a reranker is on, otherwise 10_generate.py.
