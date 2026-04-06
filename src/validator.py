"""Validation orchestration that applies all rules to each deliverable."""

from src.parser import load_json, load_yaml
from src.rule_engine import (
    check_required_fields,
    check_naming_rules,
    check_status,
    check_version,
    check_date
)

def validate(data_path, rules_path):
    """Validate deliverables from data_path using rules from rules_path."""
    data = load_json(data_path)
    rules = load_yaml(rules_path)

    results = []

    for item in data:
        # Collect all rule violations for the current item.
        errors = []

        errors.extend(check_required_fields(item, rules.get("required_fields", [])))
        errors.extend(check_naming_rules(item, rules.get("naming_rules", {})))
        errors.extend(check_status(item, rules.get("status_allowed", [])))
        errors.extend(check_version(item, rules.get("version_rules", {})))
        errors.extend(check_date(item, rules.get("date_rules", {})))

        results.append({
            "id": item.get("id", "UNKNOWN"),
            "valid": len(errors) == 0,
            "total_errors": len(errors),
            "errors": errors
        })

    return results