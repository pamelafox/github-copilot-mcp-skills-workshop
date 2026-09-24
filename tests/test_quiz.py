import src.quiz as quiz


def test_run_quiz_randomizes_questions_without_mutating_original(monkeypatch, capsys):
    questions = [
        {"question": "Q1", "options": {"A": "Alpha", "B": "Beta"}, "answer": "A"},
        {"question": "Q2", "options": {"A": "Gamma", "B": "Delta"}, "answer": "A"},
        {"question": "Q3", "options": {"A": "Omega", "B": "Theta"}, "answer": "A"},
    ]
    monkeypatch.setattr(quiz, "QUESTIONS", questions)

    shuffle_calls = []

    def fake_shuffle(items):
        shuffle_calls.append(list(items))
        items[:] = list(reversed(items))

    monkeypatch.setattr(quiz.random, "shuffle", fake_shuffle)
    answers = iter(["A", "A", "A"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    quiz.run_quiz()

    assert shuffle_calls
    assert quiz.QUESTIONS == questions
    out = capsys.readouterr().out
    assert "Question 1 of 3" in out
    assert "Q3" in out


def test_run_quiz_shows_correct_answer_when_user_is_wrong(monkeypatch, capsys):
    questions = [
        {"question": "Q1", "options": {"A": "Alpha", "B": "Beta"}, "answer": "A"},
        {"question": "Q2", "options": {"A": "Gamma", "B": "Delta"}, "answer": "A"},
    ]
    monkeypatch.setattr(quiz, "QUESTIONS", questions)
    answers = iter(["B", "A"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    quiz.run_quiz()

    out = capsys.readouterr().out
    assert "Wrong! The correct answer was A) Alpha" in out
