import json
from datetime import datetime
from src.ai_summary import generate_ai_summary


def generate_summary(results):
    total = len(results)
    passed = sum(1 for r in results if r["valid"])
    failed = total - passed

    return {
        "total_items": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round((passed / total) * 100, 2) if total > 0 else 0
    }


def generate_report(results, output_path="reports/validation_report.json"):
    summary = generate_summary(results)

    ai_part = generate_ai_summary({
        "summary": summary,
        "details": results
    })

    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": summary,
        "details": results,
        **ai_part  # merge AI output
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    return report