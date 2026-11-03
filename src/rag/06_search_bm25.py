# Purpose: step 6a. Keyword search for one question.
#
# Input:  the question text, plus the BM25 index from step 3.
# Output: the top-k chunk ids and scores.
#
# This is one of three search choices (see also 07 and 08).
# Run it when the config says search: bm25.
# Next: 10_generate.py (no reranker on the BM25-only setup).
