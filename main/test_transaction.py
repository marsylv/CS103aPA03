import tracker
import pytest

def test_exit(monkeypatch, capsys):
    user_input = "exit"
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    main()

    captured = capsys.readouterr()
    assert captured.out == "Exiting the program now!"