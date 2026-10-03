import pytest

from paperclip_sandbox.greeting import greet


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Ada", "Hello, Ada!"),
        ("Grace", "Hello, Grace!"),
    ],
)
def test_greet_returns_greeting(name: str, expected: str) -> None:
    assert greet(name) == expected


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="name must not be empty"):
        greet("")
