# Purpose: baseline. The LLM writes pandas code, and we run that code on the CSV.
#
# Input:  the question, the filtered table from 01_load_data.py,
#         and the model from the config.
# Output: the value the code printed, plus token counts and seconds.
#
# This is the strong baseline. It should beat RAG on questions that need
# many rows (averages, trends). The model does not see row chunks here.
# Next: 13_evaluate.py.
