from MyAgenticAIProject import main


def test_run_default(capsys):
    rc = main.run([])
    assert rc == 0


def test_run_name(capsys):
    rc = main.run(["--name", "TestAgent"])
    assert rc == 0