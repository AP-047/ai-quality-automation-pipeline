from transformers import pipeline

# Optional LLM (can fail silently)
try:
    generator = pipeline("text-generation", model="google/flan-t5-base")
except Exception:
    generator = None


def generate_ai_summary(report):
    summary = report.get("summary", {})
    details = report.get("details", [])

    # ✅ RULE-BASED CORE (reliable)
    failed = summary.get("failed", 0)
    total = summary.get("total_items", 0)

    error_list = []
    for item in details:
        if not item["valid"]:
            error_list.extend(item["errors"])

    common_errors = list(set(error_list))[:2]

    base_summary = (
        f"{failed} out of {total} deliverables failed validation. "
        f"Key issues include: {', '.join(common_errors)}. "
        f"Overall quality status is {'acceptable' if failed == 0 else 'needs improvement'}."
    )

    # ✅ OPTIONAL LLM ENHANCEMENT
    if generator:
        try:
            prompt = f"Improve this summary professionally:\n{base_summary}"

            result = generator(
                prompt,
                max_new_tokens=60,
                do_sample=False
            )

            return {
                "ai_summary": result[0]["generated_text"].replace(prompt, "").strip()
            }
        except Exception:
            pass

    # fallback
    return {
        "ai_summary": base_summary
    }