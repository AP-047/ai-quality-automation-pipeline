# AI Quality Automation Pipeline

A small FastAPI-based project that validates deliverable records against configurable rules, generates a structured report, and adds an AI-written summary using a local Ollama model.

## What it does

- Validates JSON deliverables against YAML rules.
- Checks required fields, naming patterns, status values, version format, and date format.
- Generates a report with pass/fail stats and per-item validation errors.
- Creates a short AI summary from the validation result.
- Exposes the validation flow through a FastAPI endpoint for easy integration.

## How it works

1. Sample deliverables are loaded from `data/sample_deliverables.json`.
2. Validation rules are read from `rules/validation_rules.yaml`.
3. The rule engine checks each record and collects errors.
4. A report is generated and written to `reports/validation_report.json`.
5. The AI summary is created through Ollama using a local model.

## Run locally

```bash
python -m venv env-ai-quality-automation-pipeline
env-ai-quality-automation-pipeline\Scripts\activate
pip install -r requirements.txt
uvicorn api.app:app --reload
```

Open:

- `http://127.0.0.1:8000` for the health check
- `http://127.0.0.1:8000/validate` to run the validation pipeline
- `http://127.0.0.1:8000/docs` for the API documentation

## Requirements

- Python 3.12+
- `uvicorn`
- `requests`
- `PyYAML`
- Ollama running locally on `http://127.0.0.1:11434`

## Project structure

- `api/app.py` - FastAPI app and endpoints
- `src/validator.py` - Validation orchestration
- `src/rule_engine.py` - Individual rule checks
- `src/report_generator.py` - Report creation
- `src/ai_summary.py` - AI summary generation
- `data/sample_deliverables.json` - Example input data
- `rules/validation_rules.yaml` - Validation rules
- `workflows/Quality Automation Workflow.json` - n8n workflow that calls the API

## Resume-friendly summary

This project demonstrates automated data quality validation, API development with FastAPI, rule-based processing, report generation, and AI-assisted summarization.
