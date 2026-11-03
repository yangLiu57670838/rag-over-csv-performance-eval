# Purpose: step 3. Build a keyword index over the chunks.
#
# Input:  chunk texts from 02_make_chunks.py.
# Output: a BM25 index (rank_bm25), saved under indexes/.
#
# Used when the config search is "bm25" or "hybrid".
# Dense search does not need this file.
# Next at question time: 06_search_bm25.py.
