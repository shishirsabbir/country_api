# imports
import datetime
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, validator


# pagination model
class PageSchema(BaseModel):
    page: int = Field(..., ge=1)
    page_length: int = Field(..., ge=1)
    page_count: int = Field(..., ge=1)
    total: int = Field(..., ge=0)


# schema model
class CountrySchema(BaseModel):
    id: str | None = None
    name: str
    code: str = Field(..., min_length=2, max_length=2)
    phone_code: str
    short_description: str
    full_description: str
    flag_svg: str
    cover_images: list[str]
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @field_validator("code", mode="before")
    @classmethod
    def code_to_upper(cls, v):
        if isinstance(v, str):
            return v.upper()

        return v


# countries response schema
class CountriesResponse(BaseModel):
    status: Literal["success", "fail", "error"]
    message: str | None = None
    data: list[CountrySchema]
    pagination: PageSchema


# country response schema
class CountryResponse(BaseModel):
    status: Literal["success", "fail", "error"]
    message: str | None = None
    data: CountrySchema | None = None
