# imports
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


# NOTE:
# Whenever you update or add new environment variables in this Settings class,
# make sure to also update the corresponding entries in the config.env file.
# This keeps your configuration consistent and avoids missing environment variables.


# setting class
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="./config.env", extra="ignore")

    app_name: str = "nCountry"
    app_version: str = "0.0.1"
    database_url: str = Field(..., alias="DB_URL")


settings = Settings()
