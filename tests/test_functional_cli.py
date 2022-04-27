from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "beer added" in result.stdout


def test_list_beer():
    # Arrange
    runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )

    # Act
    result = runner.invoke(main, ["list", "--style", "Witbier"])

    # Assert
    assert result.exit_code == 0

    # TODO: Implementar a verificação dentro da tabela de saída
    # assert "Witbier" in result.stdout
