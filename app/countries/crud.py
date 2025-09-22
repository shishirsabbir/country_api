# imports
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.countries.model import Country
from app.countries.schema import CountrySchema


# get countries function
async def get_Countries(
    db: AsyncSession, offset: int = 0, limit: int = 10
) -> list[Country]:
    """
    Fetches a paginated list of countries
    """

    query = select(Country).offset(offset).limit(limit)
    result = await db.execute(query)
    return list(result.scalars().all())


# get country function
async def get_Country_Count(db: AsyncSession):
    """
    Gets the total number of countries in the database.
    """
    query = select(func.count()).select_from(Country)
    result = await db.execute(query)
    return result.scalar_one()


# get country function
async def get_Country(db: AsyncSession, country_id: str) -> Country | None:
    """
    Fetches a single country by its ID.
    """
    query = select(Country).where(Country.id == country_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


# create country function
async def create_Country(db: AsyncSession, country_input: CountrySchema) -> Country:
    """
    Creates a new country in the database from a pydantic schema.
    """
    country_data = country_input.model_dump(exclude={"id", "created_at", "updated_at"})
    db_country = Country(**country_data)
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country
