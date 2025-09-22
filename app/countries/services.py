# imports
from app.countries import crud
from sqlalchemy.ext.asyncio import AsyncSession
from app.countries.schema import CountrySchema


# service functions for the router
async def fetch_All_Countries(
    db: AsyncSession, page: int, page_length: int
) -> tuple[list[CountrySchema], int]:
    """
    Service function to get a paginated list of countries.
    """
    offset = (page - 1) * page_length
    countries = await crud.get_Countries(db, offset=offset, limit=page_length)
    total_count = await crud.get_Country_Count(db)

    # convert each sqlalchemy model to a pydantic schema
    countries_as_schema = [
        CountrySchema.model_validate(country) for country in countries
    ]

    return countries_as_schema, total_count


async def fetch_Country_By_ID(
    db: AsyncSession, country_id: str
) -> CountrySchema | None:
    """
    Service function to get a single country by it's ID
    """
    country = await crud.get_Country(db, country_id=country_id)
    if country:
        return CountrySchema.model_validate(country)
    return None


async def add_New_Country(
    db: AsyncSession, country_input: CountrySchema
) -> CountrySchema:
    """
    Service function to create a new country.
    """
    new_country = await crud.create_Country(db, country_input=country_input)
    return CountrySchema.model_validate(new_country)
