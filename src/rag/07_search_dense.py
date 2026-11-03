# Purpose: step 6b. Vector search for one question.
#
# Input:  the question text, embedded with the same BGE model as step 4,
#         plus the FAISS index from step 5.
# Output: the top-k nearest chunk ids and scores.
#
# Run it when the config says search: dense.
# Next: 10_generate.py.
