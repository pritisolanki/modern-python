from click.testing import CliRunner
from modern_python import console


def test_main_succeeds():
    runner = CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
