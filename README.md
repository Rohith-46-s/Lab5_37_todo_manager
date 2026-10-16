# Lab 5 — Static Code Analysis (todo_manager.py)

## Project Title & Description

**Lab 5: Static Code Analysis** — A Python `todo_manager.py` script analyzed and refactored using three industry-standard static analysis tools: **Pylint**, **Bandit**, and **Flake8**. The project demonstrates detecting and resolving code quality, security, and PEP 8 style issues to maximize code maintainability and robustness.

## Repository Link

[https://github.com/Rohith-46-s/Lab5_37_todo_manager.git](https://github.com/Rohith-46-s/Lab5_37_todo_manager.git)

## Objective

Enhance Python code quality, security, and PEP 8 style compliance by utilizing static analysis tools (Pylint, Bandit, and Flake8) to detect and rectify common programming issues such as bare `except:` statements, mutable default arguments, insecure `eval()` usage, hardcoded secrets, unused imports, and formatting violations.

## Tools Used & Installation

```bash
# Create and activate a virtual environment
python3 -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install static analysis tools
pip install pylint bandit flake8
```

## Static Analysis Summary Table

| Tool | Metric | Before | After |
|------|--------|--------|-------|
| Pylint | Score | 5.47 / 10 | **10.00 / 10** |
| Bandit | Vulnerabilities | 6 issues (1 High severity) | **0 issues** |
| Flake8 | Style violations | 6 violations | **0 violations** |

### Key Fixes Applied
- Replaced bare `except:` with specific exception types (`ValueError`, `OSError`, `SyntaxError`)
- Replaced `eval()` with `ast.literal_eval()` for safe parsing
- Fixed mutable default arguments (`=[]` → `None` initializer)
- Removed hardcoded API key; moved to environment variable
- Removed `subprocess` with `shell=True` (security risk)
- Added module and function docstrings
- Converted %-formatting to f-strings; used `enumerate`
- Added explicit `encoding="utf-8"` to `open()` calls
- Removed unused imports (`os`, `json`)

## Deliverables Included

| File | Description |
|------|-------------|
| `todo_manager.py` | Refactored Python script with all static analysis issues resolved |
| `ISSUES_TABLE.md` | Complete summary table of all fixed issues (Issue, Type, Line(s), Description, Fix Approach) |
| `reflection_lab5.txt` | Answers to the 4 lab reflection questions |
| `pylint_report.txt` | Pylint static analysis report |
| `bandit_report.txt` | Bandit security analysis report |
| `flake8_report.txt` | Flake8 style analysis report |

## How to Run Analysis

Regenerate all three reports from the terminal in the repository root:

```bash
# Pylint code quality report
pylint todo_manager.py > pylint_report.txt

# Bandit security report
bandit -r todo_manager.py > bandit_report.txt

# Flake8 PEP 8 style report
flake8 todo_manager.py > flake8_report.txt
```

Expected clean results:
- Pylint: `10.00/10`
- Bandit: `No issues identified.`
- Flake8: no output (zero violations)

## How to Run the Script

```bash
python todo_manager.py
```
