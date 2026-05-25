from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Message:
    role: str
    content: str
    provider: str = "local"


Provider = Callable[[list[Message]], Message]


def echo_provider(messages: list[Message]) -> Message:
    latest = messages[-1].content if messages else ""
    return Message("assistant", f"echo: {latest}", "echo")


def save_jsonl(path: str | Path, messages: list[Message]) -> None:
    Path(path).write_text("\n".join(json.dumps(asdict(m)) for m in messages) + "\n", encoding="utf-8")


def load_jsonl(path: str | Path) -> list[Message]:
    text = Path(path).read_text(encoding="utf-8")
    return [Message(**json.loads(line)) for line in text.splitlines() if line.strip()]


def run_turn(history: list[Message], prompt: str, provider: Provider = echo_provider) -> list[Message]:
    next_history = [*history, Message("user", prompt)]
    return [*next_history, provider(next_history)]
