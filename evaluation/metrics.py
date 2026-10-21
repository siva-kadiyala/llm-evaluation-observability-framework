from difflib import SequenceMatcher


def normalize_text(text: str) -> str:
    """Clean up whitespace and convert text to lowercase."""
    return " ".join(text.lower().split())


def exact_match(expected: str, actual: str) -> bool:
    """Check whether two answers match after basic normalization."""
    return normalize_text(expected) == normalize_text(actual)


def similarity_score(expected: str, actual: str) -> float:
    """Return a simple text similarity score between 0 and 1."""
    expected = normalize_text(expected)
    actual = normalize_text(actual)

    if not expected and not actual:
        return 1.0

    if not expected or not actual:
        return 0.0

    return round(SequenceMatcher(None, expected, actual).ratio(), 4)
