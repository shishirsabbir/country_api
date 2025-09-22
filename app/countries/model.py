# imports
import uuid
from app.database.base import BaseDatabase
from sqlalchemy import String, Integer, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship


# defining country model
class Country(BaseDatabase):
    __tablename__ = "countries"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(
        String(2), nullable=False, unique=True
    )  # Alpha-2 code
    phone_code: Mapped[str] = mapped_column(String(8), nullable=False)
    short_description: Mapped[str] = mapped_column(String(255), nullable=False)
    full_description: Mapped[str] = mapped_column(String, nullable=False)
    flag_svg: Mapped[str] = mapped_column(String, nullable=False)
    cover_images: Mapped[list[str]] = mapped_column(JSON, nullable=False)

    # relationships
    populations: Mapped[list["Population"]] = relationship(
        "Population", back_populates="country"
    )
    gdps: Mapped[list["GDP"]] = relationship("GDP", back_populates="country")


# defining country population model
class Population(BaseDatabase):
    __tablename__ = "populations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
    )
    country_id: Mapped[str] = mapped_column(ForeignKey("countries.id"), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)

    # relationship
    country: Mapped["Country"] = relationship("Country", back_populates="populations")


# defining country gdp model
class GDP(BaseDatabase):
    __tablename__ = "gdps"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
    )
    country_id: Mapped[str] = mapped_column(ForeignKey("countries.id"), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    gdp: Mapped[str] = mapped_column(String, nullable=False)

    # relationship
    country: Mapped["Country"] = relationship("Country", back_populates="gdps")
