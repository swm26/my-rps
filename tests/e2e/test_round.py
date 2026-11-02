"""RPS-001 browser test: play a round with a fixed computer move, then replay."""

import pytest
from playwright.sync_api import expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_then_replay_uses_real_rules(live_server, page, monkeypatch):
    """Rock loses to paper, then scissors beats paper in a fresh round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    page.goto(live_server)

    page.locator('[name="move"][value="rock"]').click()
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_text("Computer wins")).to_be_visible()
    expect(page.get_by_text("You chose")).to_be_visible()
    expect(page.get_by_text("Computer chose")).to_be_visible()
    expect(page.get_by_text("game rules not built yet")).to_have_count(0)

    page.locator('[name="move"][value="scissors"]').click()
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_text("You win!")).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_have_count(0)
