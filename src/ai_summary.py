from transformers import pipeline

# Load once (important)
generator = pipeline("text2text-generation", model="google/flan-t5-base")


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    prompt = f"""
    You are a quality engineer.

    A validation system produced this report:
    
    Total items: {summary['total_items']}
    Passed: {summary['passed']}
    Failed: {summary['failed']}

    Errors:
    {details}

    Write a short professional summary highlighting:
    - how many failed
    - key issues
    - overall quality status
    """

    result = generator(prompt, max_length=120, do_sample=False)

    return {
        "ai_summary": result[0]["generated_text"]
    }