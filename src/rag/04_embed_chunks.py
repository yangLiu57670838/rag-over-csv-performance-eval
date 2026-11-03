# Purpose: step 4. Turn each chunk into a vector.
#
# Input:  chunk texts from 02_make_chunks.py.
# Output: one embedding per chunk, from a BGE model (sentence-transformers).
#
# Used when the config search is "dense" or "hybrid".
# BM25-only runs skip this file.
# Next: 05_build_faiss_index.py.
