from fastapi import FastAPI
from src.validator import validate
from src.report_generator import generate_report

app = FastAPI(title="AI Quality Automation API")


@app.get("/")
def root():
    return {"message": "Quality Automation API is running"}


@app.get("/validate")
def run_validation():
    results = validate(
        "data/sample_deliverables.json",
        "rules/validation_rules.yaml"
    )

    report = generate_report(results)

    return report