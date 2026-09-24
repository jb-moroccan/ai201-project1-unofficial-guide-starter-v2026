def judge(question, expects, answer, results) -> bool:
    """
    Judge whether an answer is correct.

    Args:
        question: The question that was asked
        expects: The expected answer or criteria
        answer: The actual answer provided
        results: The retrieval results

    Returns:
        bool: True if the answer is correct, False otherwise
    """
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()
