"""RPS-001 tests: the game rules and a submitted round."""

import pytest

import app as app_module
from game import determine_winner


@pytest.fixture(name="round_client")
def round_client_fixture():
    """Flask test client for submitting rounds."""
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client()


@pytest.mark.unit
@pytest.mark.parametrize(
    "player, computer, expected",
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner(player, computer, expected):
    """All nine matchups return the expected result."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
@pytest.mark.parametrize(
    "player, computer, expected_text",
    [
        ("rock", "paper", "Computer wins"),
        ("rock", "scissors", "You win!"),
        ("paper", "paper", "It’s a tie"),
    ],
)
def test_round_uses_real_rules(
    round_client, monkeypatch, player, computer, expected_text
):
    """A submitted round uses determine_winner and shows the result."""
    monkeypatch.setattr(app_module.random, "choice", lambda moves: computer)

    response = round_client.post("/", data={"move": player})
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert expected_text in page
    assert "game rules not built yet" not in page
