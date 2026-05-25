from __future__ import annotations

import argparse
from pathlib import Path
from .core import load_jsonl, run_turn, save_jsonl


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Provider-neutral chat transcript hub.")
    parser.add_argument("transcript")
    parser.add_argument("prompt")
    args = parser.parse_args(argv)
    path = Path(args.transcript)
    history = load_jsonl(path) if path.exists() else []
    updated = run_turn(history, args.prompt)
    save_jsonl(path, updated)
    print(updated[-1].content)
    return 0
