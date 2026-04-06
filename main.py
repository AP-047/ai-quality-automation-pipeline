"""CLI entrypoint to run validation and print the final report."""

from src.validator import validate
from src.report_generator import generate_report
import json

if __name__ == "__main__":
    # Validate sample deliverables using configured rules.
    results = validate(
        "data/sample_deliverables.json",
        "rules/validation_rules.yaml"
    )

    # Build the final report, including the AI summary.
    report = generate_report(results)

    # Print a readable JSON report for local runs.
    print(json.dumps(report, indent=2))