# imports
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_db
from app.countries.services import (
    fetch_All_Countries,
    fetch_Country_By_ID,
    add_New_Country,
)
from app.countries.schema import (
    CountriesResponse,
    CountryResponse,
    CountrySchema,
    PageSchema,
)


# defining router
router = APIRouter()


@router.get("/", response_model=CountriesResponse)
async def get_Countries(
    db: AsyncSession = Depends(get_db),
    page: int = Query(10, ge=1, description="Page Number"),
    page_length: int = Query(10, ge=1, le=100, description="Items per page"),
):
    """
    Get a paginated list of all countries.
    """

    countries, total = await fetch_All_Countries(db, page, page_length)
    page_count = total + page_length - 1

    return CountriesResponse(
        status="success",
        data=countries,
        pagination=PageSchema(
            page=page, page_length=page_length, page_count=page_count, total=total
        ),
    )


@router.get("/{country_id}", response_model=CountryResponse)
async def get_Country(country_id: str, db: AsyncSession = Depends(get_db)):
    """
    Get details for a single country by its ID
    """

    country = await fetch_Country_By_ID(db, country_id)
    if not country:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"country with ID {country_id} not found!",
        )

    return CountryResponse(status="success", data=country)


@router.post("/", response_model=CountryResponse, status_code=status.HTTP_201_CREATED)
async def create_Country(
    country_input: CountrySchema, db: AsyncSession = Depends(get_db)
):
    """
    Create a new country.
    """
    new_country = await add_New_Country(db, country_input)
    return CountryResponse(status="success", data=new_country)
