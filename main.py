from src.validator import validate
import json

if __name__ == "__main__":
    results = validate(
        "data/sample_deliverables.json",
        "rules/validation_rules.yaml"
    )

    print(json.dumps(results, indent=2))