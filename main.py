from src.validator import validate
from src.report_generator import generate_report
import json

if __name__ == "__main__":
    results = validate(
        "data/sample_deliverables.json",
        "rules/validation_rules.yaml"
    )

    report = generate_report(results)

    print(json.dumps(report, indent=2))