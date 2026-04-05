def check_required_fields(item, required_fields):
    errors = []
    for field in required_fields:
        if field not in item or not item[field]:
            errors.append(f"Missing or empty field: {field}")
    return errors


def check_naming_rules(item, naming_rules):
    errors = []
    name = item.get("name", "").lower()

    if not any(keyword in name for keyword in naming_rules.get("name_must_contain", [])):
        errors.append("Invalid naming convention")

    return errors


def check_status(item, allowed_status):
    errors = []
    if item.get("status") not in allowed_status:
        errors.append(f"Invalid status: {item.get('status')}")
    return errors

from datetime import datetime


def check_version(item, version_rules):
    errors = []
    version = item.get("version", "")

    if not version.startswith(version_rules.get("must_start_with", "")):
        errors.append(f"Invalid version format: {version}")

    return errors


def check_date(item, date_rules):
    errors = []
    date_str = item.get("last_updated", "")

    try:
        datetime.strptime(date_str, date_rules.get("format"))
    except Exception:
        errors.append(f"Invalid date format: {date_str}")

    return errors