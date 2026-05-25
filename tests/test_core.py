from chatmux.core import load_jsonl, run_turn, save_jsonl


def test_chat_roundtrip(tmp_path):
    history = run_turn([], "hello")
    assert history[-1].content == "echo: hello"
    path = tmp_path / "chat.jsonl"
    save_jsonl(path, history)
    assert load_jsonl(path)[0].role == "user"
