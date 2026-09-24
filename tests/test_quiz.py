from src.quiz import normalize_answer


def test_normalize_answer_accepts_lowercase_letters():
    assert normalize_answer("a") == "A"
    assert normalize_answer(" A ") == "A"
