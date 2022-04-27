import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database

    Args:
        name (str): _description_
        style (str): _description_
    """
    if add_beer_to_database(name, style, flavor, image, cost):
        print(":beer: beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database

    Args:
        style (str): _description_
    """
    beers = get_beers_from_database(style)
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")

    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
