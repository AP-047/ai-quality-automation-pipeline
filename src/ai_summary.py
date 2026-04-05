from transformers import pipeline

# Use text-generation (compatible with your version)
generator = pipeline("text-generation", model="google/flan-t5-base")


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    # Extract errors cleanly
    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    error_text = ", ".join(set(error_list))

    prompt = f"""
    Total items: {summary['total_items']}
    Passed: {summary['passed']}
    Failed: {summary['failed']}

    Common issues: {error_text}

    Write a short professional summary.
    """

    result = generator(
        prompt,
        max_new_tokens=80,
        # min_length=30,
        do_sample=False
    )

    return {
        "ai_summary": result[0]["generated_text"].strip()
    }