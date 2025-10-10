# MyAgenticAIProject

Minimal scaffold for an agentic AI project.

Quickstart

1. Activate your existing `.venv` virtual environment.

On Windows PowerShell (assuming the venv is at `.venv` in the workspace root):

```powershell
.\.venv\Scripts\Activate.ps1
```

2. Install dev dependencies:

```powershell
pip install -e .[dev]
```

3. Run tests:

```powershell
pytest -q
```

Usage

```powershell
python -m MyAgenticAIProject.main --name "Alice"
```
