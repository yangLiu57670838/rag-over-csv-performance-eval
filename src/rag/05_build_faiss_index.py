# Purpose: step 5. Store the chunk vectors for nearest-neighbour search.
#
# Input:  embeddings from 04_embed_chunks.py.
# Output: a FAISS index under indexes/, aligned with chunk ids.
#
# Next at question time: 07_search_dense.py (or 08_search_hybrid.py).
