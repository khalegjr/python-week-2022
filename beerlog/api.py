from typing import List, Optional
from fastapi import FastAPI, Response, status # ASGI
from beerlog.core import get_beers_from_database, add_beer_to_database
from beerlog.serializers import BeerIn, BeerOut


api = FastAPI(title="Beerlog")

@api.get("/beers", response_model=List[BeerOut])
def list_beers(style: Optional[str] = None):
    """Lists beers from the database

    Returns:
        _type_: _description_
    """
    beers = get_beers_from_database(style)
    return beers

@api.post("/beers", response_model=BeerOut)
def add_beer(beer_in: BeerIn, response: Response):
    
    if add_beer_to_database(**beer_in.dict()):
        response.status_code = status.HTTP_201_CREATED
