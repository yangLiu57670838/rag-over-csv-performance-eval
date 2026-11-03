# Purpose: download the source CSVs and save them under data/raw/.
#
# This is the step before the RAG pipeline. It only fetches files.
# Cutting columns and years happens in src/rag/01_load_data.py.
#
# Sources:
#   - OWID CO₂ data (main): country × year
#   - OWID notable AI models: one row per model
#   - OWID energy data (optional): country × year
#
# After a download, write the date and version into data/README.md.
