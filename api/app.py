"""FastAPI entrypoint for running validation and returning reports."""

from fastapi import FastAPI
from src.validator import validate
from src.report_generator import generate_report

app = FastAPI(title="AI Quality Automation API")


@app.get("/")
def root():
    """Health endpoint to confirm the API is up."""
    return {"message": "Quality Automation API is running"}


@app.get("/validate")
def run_validation():
    """Run the full validation pipeline and return the generated report."""
    results = validate(
        "data/sample_deliverables.json",
        "rules/validation_rules.yaml"
    )

    report = generate_report(results)

    return report