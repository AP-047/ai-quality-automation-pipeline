import requests

# Ollama config
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "gemma:2b"


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    # Extract errors
    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    error_text = ", ".join(set(error_list))

    # Prompt (keep it short for small models)
    prompt = (
        f"{summary['failed']} out of {summary['total_items']} deliverables failed validation. "
        f"Issues: {error_text}. "
        f"Write a short professional summary."
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        output = response.json()

        ai_text = output.get("response", "").strip()

        # ✅ Safety check (in case model returns empty)
        if not ai_text:
            raise Exception("Empty response")

        return {
            "ai_summary": ai_text
        }

    except Exception as e:
        print("Ollama error:", str(e))

        # ✅ Fallback (always reliable)
        return {
            "ai_summary": (
                f"{summary.get('failed', 0)} out of {summary.get('total_items', 0)} "
                f"deliverables failed validation. Key issues include: {error_text}."
            )
        }