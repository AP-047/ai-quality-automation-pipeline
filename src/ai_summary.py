import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    # Extract errors
    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    error_text = ", ".join(set(error_list))

    prompt = (
        f"{summary['failed']} out of {summary['total_items']} deliverables failed validation. "
        f"Key issues: {error_text}. "
        f"Provide a short professional summary."
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=10
        )

        output = response.json()

        return {
            "ai_summary": output.get("response", "").strip()
        }

    except Exception:
        # fallback (important)
        return {
            "ai_summary": (
                f"{summary.get('failed', 0)} out of {summary.get('total_items', 0)} "
                f"deliverables failed validation. Key issues include: {error_text}."
            )
        }