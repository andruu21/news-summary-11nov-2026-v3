# news-summary-11nov-2026-v3

A deterministic, stdlib-only Python script that writes a plain-English
world news summary for 11 November 2026 to `/output/entry.txt`.

## Usage

```bash
python3 main.py
```

Requires Python 3.13+ and write access to `/output`. No network access,
no randomness, no clock reads — repeated runs produce byte-identical
output.

## License

MIT — see [LICENSE](LICENSE).
