"""Creates a short AI summary for the generated validation report."""

import requests

# Local Ollama endpoint and model used for summary generation.
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "gemma:2b"

def generate_ai_summary(report):
    """Call Ollama and return a short text summary for report findings."""
    summary = report.get("summary", {})
    details = report.get("details", [])

    # Collect all validation errors from failed items.
    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    error_text = ", ".join(set(error_list))

    prompt = (
        f"{summary['failed']} out of {summary['total_items']} deliverables failed validation. "
        f"Issues: {error_text}. "
        f"Write ONLY 1-2 concise professional sentences."
        f"No bullet points. No formatting. Plain text."
        f"Do not mention 'user'. DOn not mention the exact terms from the result."
        f"Directly start your analysis of the output. Use neutral engineering tone."
    )

    # Send the prompt to Ollama and parse the generated text.
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

    if not ai_text:
        raise RuntimeError("Empty response from Ollama")

    return {
        "ai_summary": ai_text
    }