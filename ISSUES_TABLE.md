# ISSUES_TABLE.md

Lab 5: Static Code Analysis — Issues Fixed in `todo_manager.py`

All issues reported by Pylint, Bandit, and Flake8 were fixed. The tables below
list every issue found across the three tools, its type, original line(s) in
the pre-fix version of `todo_manager.py`, a description, and the fix approach.

## Pylint findings

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| missing-module-docstring (C0114) | Style | 1 | Module had no docstring | Added a module-level docstring describing the file's purpose |
| missing-function-docstring (C0116) | Style | 11, 18, 25, 33, 39, 43, 51, 59 | Eight functions lacked docstrings | Added docstrings (Args/Returns) to every public function |
| dangerous-default-value (W0102) | Bug | 18, 25 | Mutable default argument `task_list=[]` shared across calls | Changed defaults to `None` and initialize `[]` inside the function |
| bare-except (W0702) | Bug | 28, 39, 47, 55 | Bare `except:` catches all exceptions including KeyboardInterrupt/SystemExit | Replaced with specific types: `ValueError`, `OSError`, `SyntaxError` |
| unspecified-encoding (W1514) | Style | 35, 45 | `open()` called without explicit encoding | Added `encoding="utf-8"` to all `open()` calls |
| eval-used (W0123) | Security | 37, 53 | `eval()` on untrusted input allows arbitrary code execution | Replaced `eval()` with `ast.literal_eval()` |
| consider-using-enumerate (C0200) | Style | 60 | `range(len(tasks))` indexing is unpythonic | Replaced with `enumerate(tasks, start=1)` |
| consider-using-f-string (C0209) | Style | 61 | `%`-style string formatting instead of f-strings | Converted to f-string |
| subprocess-run-check (W1510) | Style | 70 | `subprocess.run()` called without `check` | Removed subprocess usage entirely |
| unused-import os (W0611) | Style | 1 | `os` imported but unused | Removed (later re-added for `os.getenv`, so now used) |
| unused-import json (W0611) | Style | 4 | `json` imported but unused | Removed `json` import |

## Bandit findings

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| B404 blacklist (subprocess import) | Security | 3 | Importing subprocess presents injection risk | Removed `subprocess` import and its usage |
| B110 try_except_pass | Security | 28 | `try/except/pass` silently swallows errors | Replaced bare except with `except ValueError` (intentional no-op on missing item) |
| B307 blacklist (eval) | Security | 37, 53 | `eval()` on potentially untrusted data | Replaced with `ast.literal_eval()` |
| B607 start_process_with_partial_path | Security | 70 | Process started with partial executable path | Removed subprocess usage |
| B602 subprocess_popen_with_shell_equals_true | Security | 70 | `shell=True` enables shell injection | Removed `shell=True` / subprocess entirely |
| Hardcoded sensitive data (API_KEY) | Security | 10 | Secret/API key hardcoded in source | Moved to `os.getenv("TODO_API_KEY", "")` |

## Flake8 findings

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| F401 unused import os | Style | 1 | `os` imported but unused | Removed (re-added once actually used for `getenv`) |
| F401 unused import json | Style | 4 | `json` imported but unused | Removed `json` import |
| E722 bare `except` | Bug | 28, 39, 47, 55 | Bare `except` statements | Replaced with specific exception types |

## Verification (post-fix)

- Pylint: `10.00/10`, no messages
- Bandit: `No issues identified.` (0 Low, 0 Medium, 0 High)
- Flake8: no output (zero violations)
