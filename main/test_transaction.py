import tracker
import pytest

def test_exit(monkeypatch, capsys):
    user_input = "exit"
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    tracker.process_args()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Exiting the program now!"