# Purpose: baseline, not a retrieval step. The LLM answers with no chunks.
#
# Input:  the question and the model from the config.
# Output: the model's answer, plus token counts and seconds.
#
# This measures what the model already remembers. Compare it with RAG
# to see whether search actually helped.
# Next: 13_evaluate.py.
