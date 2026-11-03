# Purpose: step 7. Reorder the retrieved chunks with a cross-encoder.
#
# Input:  the question plus the hybrid hit list from 08_search_hybrid.py.
# Output: the same chunks in a new order, scored by a BGE reranker.
#
# Only the "hybrid + reranker" experiments use this step.
# Next: 10_generate.py.
