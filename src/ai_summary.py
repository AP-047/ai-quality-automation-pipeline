from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    # ✅ Extract ONLY errors (clean input)
    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    error_text = ", ".join(set(error_list))

    prompt = f"""
    Summarize the following validation results in 2-3 sentences:

    Total items: {summary['total_items']}
    Passed: {summary['passed']}
    Failed: {summary['failed']}

    Common issues: {error_text}

    Provide a concise professional summary.
    """

    result = generator(
        prompt,
        max_length=80,
        do_sample=False
    )

    return {
        "ai_summary": result[0]["generated_text"].strip()
    }