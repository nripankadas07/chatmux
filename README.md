# chatmux

Provider-neutral chat transcript hub with no-key local mocks.

Inspired by the practical, user-sovereign spirit of `LibreChat`,
but intentionally scoped as a small reference tool you can read, run, test,
and extend from a fresh clone.

## Why It Exists

Big internet services are convenient because they hide infrastructure.
`chatmux` keeps the useful part visible: local files, explicit
inputs, repeatable output, and no account requirement for the core workflow.

## Install From Source

```bash
git clone https://github.com/nripankadas07/chatmux
cd chatmux
python -m pip install -e ".[dev]"
```

## Quick Check

```bash
python -m pytest -q
chatmux --help
```

## Scope

This is not a clone of `LibreChat` and does not pretend to
replace a mature production project. It is a compact, auditable foundation
for one internet-ownership workflow.

## Quality

- Typed Python package with a small public API.
- CLI entry point.
- Unit tests for core behavior.
- GitHub Actions CI.
- MIT licensed.

## License

MIT. See [LICENSE](LICENSE).
