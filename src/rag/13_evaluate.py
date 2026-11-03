# Purpose: step 9. Score one finished run and save it under results/.
#
# Input:  gold rows from eval/questions.jsonl, retrieved chunk ids,
#         and the model's answers (from step 10, 11, or 12).
# Output: a results CSV (and later, charts) for this config.
#
# Metrics:
#   Accuracy        numeric answer within 1% of the gold value;
#                   yes/no questions use exact match
#   Recall@k        did search return the rows listed in rows_needed
#   Made-up numbers a number was given when the right rows were missing,
#                   or under storage C (metadata only)
#   Refusal         unanswerable questions get "I don't know"
#   Cost and speed  tokens and seconds per question
