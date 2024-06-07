from pydantic_settings import BaseSettings, SettingsConfigDict


class Setings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", # Can be replaced with an invalid path/string
    )
    BOT_TOKEM: str



setings = Setings()
