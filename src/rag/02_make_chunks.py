# Purpose: step 2. Turn table rows into the text that search will index.
# This is the storage comparison. A config chooses one mode.
#
# Input:  filtered table from 01_load_data.py.
# Output: a list of chunks, each tied to the source row ids (for recall@k).
#
#   A  Raw rows. Keep the header and the cell values, e.g.
#      country,year,co2_per_capita / Australia,2020,15.4
#   B  Rows as sentences, e.g.
#      "In 2020, Australia's CO₂ per person was 15.4 tonnes."
#   C  Metadata only (control). A short description of the dataset,
#      with no numbers. Used to see when the model invents a figure.
#
# Repeat the header once per chunk, and keep chunks short.
# Next: 03_build_bm25_index.py and/or 04_embed_chunks.py.
