from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str


    REF_LINK: str = "https://t.me/Binance_Moonbix_bot/start?startApp=ref_7180733078&startapp=ref_7180733078&utm_medium=web_share_copy"
    AUTO_TASK: bool = True
    AUTO_PLAY_GAME: bool = True
    DELAY_EACH_ACCOUNT: list[int] = [60, 120]

    MORE_ACCURATE_CAPTCHA_SOLVER: bool = False

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()

