from evaluation.metrics import exact_match, similarity_score


def test_exact_match_ignores_case_and_extra_spaces():
    assert exact_match("Hello World", "  hello   world ")


def test_exact_match_returns_false_for_different_answers():
    assert not exact_match("New York", "New Jersey")


def test_similarity_score_is_one_for_identical_answers():
    assert similarity_score("Python is useful", "Python is useful") == 1.0


def test_similarity_score_is_zero_for_empty_vs_nonempty():
    assert similarity_score("", "Python") == 0.0


def test_similarity_score_stays_between_zero_and_one():
    score = similarity_score("The sky is blue", "The sky looks blue")
    assert 0.0 <= score <= 1.0
