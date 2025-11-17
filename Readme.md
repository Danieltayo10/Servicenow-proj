# ServiceNow ITSM → LLM Training Data Automation Engine

This project converts raw ServiceNow Incident data into high-quality JSONL
training datasets for enterprise LLM fine-tuning.

### Features
- Uses real ITSM concepts: Incidents, Priorities, SLAs, Categories.
- Generates 3 types of training samples:
  - Incident Classification
  - Professional Rewrite
  - Domain Summary
- Outputs valid JSONL used in model training pipelines.
- Clean Python implementation.

### How to Run
1. Add your ServiceNow incident data inside `data/incidents.json`
2. Run:
```
python src/generator.py
```
3. Training dataset will be generated in `output/training_data.jsonl`
