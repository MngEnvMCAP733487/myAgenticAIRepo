"""Entry point for MyAgenticAIProject"""
from __future__ import annotations

import argparse
import sys


def run(argv: list[str] | None = None) -> int:
    """Run the simple agent CLI. Returns exit code."""
    parser = argparse.ArgumentParser(prog="myagent", description="Run the minimal agent")
    parser.add_argument("--name", default="Agent", help="Name of the agent")
    args = parser.parse_args(argv)

    print(f"Hello from {args.name}! This is MyAgenticAIProject.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())