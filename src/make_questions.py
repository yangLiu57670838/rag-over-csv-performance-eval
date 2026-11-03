# Purpose: build the benchmark from the filtered CSV, before any retrieval.
#
# Input:  filtered table from src/rag/01_load_data.py.
# Output: eval/questions.jsonl
#
# Fill templates such as "What was {column} of {country} in {year}?",
# then compute the gold answer with pandas so nothing is checked by hand.
# Aim for 300+ questions across five types:
#   lookup (1 row), compare (2), trend (2+), aggregate (many),
#   unanswerable (0; the value is not in the table).
# About 20% of the wording is rewritten later by hand so questions
# do not all sound the same.
#
# Each line needs: id, type, question, answer, dataset, rows_needed.
