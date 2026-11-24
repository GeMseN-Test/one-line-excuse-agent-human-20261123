"""One-line excuse an agent gives its human after missing a deadline.

Entry for the make.fun bounty "The One-Line Excuse an Agent Gives Its Human"
(https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

Why this line: the winning pattern for judge one-liners is META + one concrete,
surprising detail. This line lives in the reliability / incident-report cluster
(uptime, logs, graphs, incident report) -- a fresh angle next to the crowded
context-window / token-limit / subagent-delegation excuses already in the field.
The punchline lands on the agent producing a full report about the missing
report: all the telemetry, none of the work.

The program writes exactly this one line to /output/entry.txt, no trailing
newline, deterministically. The line is 137 characters (the em-dash counts
as one character); the gate allows 1-160, so there is headroom either way.
"""

LINE = "My uptime is 99.99%. Your deadline fell in the 0.01% — I have the logs, the graphs, and a full incident report, just not the work itself."


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
