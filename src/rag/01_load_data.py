# Purpose: step 1. Turn a raw download into the small table every later step uses.
#
# Input:  data/raw/ CSVs from data/download.py.
# Output: a filtered table (about 8 columns, years from 1990 on).
#
# Prefer less famous columns so the model cannot answer from memory.
# The same table feeds chunking (step 2), question building
# (src/make_questions.py), and the pandas code-tool baseline (step 12).
