# Purpose: step 8. Ask the LLM to answer from the retrieved chunks.
#
# Input:  the question, the chunk texts from search (and rerank, if used),
#         and the model named in the config (one API model, or a small
#         local model via Ollama).
# Output: the model's answer text, plus token counts and seconds.
#
# The prompt should use only the retrieved text. No tools in this step.
# The no-retrieval and code-tool baselines are steps 11 and 12.
# Next: 13_evaluate.py.
