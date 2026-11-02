# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

I predicted that if the player chooses rock and the computer chooses paper, the computer wins, because paper covers rock. `determine_winner("rock", "paper")` should return `lose`, and the page should show "Computer wins".

Plan for RPS-001:

- Implement `determine_winner(player, computer)` in `game.py` so all nine matchups in the table above return the expected `win`, `lose`, or `tie` from the player's perspective.
- Unit (positive): test all nine expected results literally, including the rock-vs-paper loss and the ties.
- Integration (positive): submit a round with a fixed computer choice and check that the page shows both choices and the correct result, using the real rule function.
- Integration (negative): a missing or unsupported move (anything other than rock, paper, or scissors) returns HTTP 400 with a helpful message, and the rules are not called.
- E2E (positive): in a real browser, play a round with a fixed computer choice, check the result, then play again to confirm rounds are independent.
- Out of scope: scoring, saved history, and renaming or restyling the interface.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/swm26/my-rps/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: determine_winner function present in `game.py`
- Checks: Full `.venv/bin/python check.py` passed (Black, Pylint, 25 non-browser tests, 6 real-browser tests). Tests: `tests/test_game.py` (unit and integration), `tests/e2e/test_round.py` (browser round and replay), plus the supplied `tests/test_shell.py` for invalid and missing moves. Browser observations: Game works fine, no issues seen.
