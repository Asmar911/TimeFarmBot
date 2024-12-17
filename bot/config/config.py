from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    LOGIN_SLEEP: list[int] = [60, 360]
    MINI_SLEEP: list[int] = [5, 15]
    BIG_SLEEP: list[int] = [10800, 18000]
    ACCOUNTS_MOOD_SEQUENTIAL: bool= True
    
    REF_ID: str = "1eYFkqTqjduuyi4DN"

    AUTO_CLAIM_REFERRAL: bool = True
    AUTO_FARM: bool = True
    AUTO_TASK: bool = False # Not working for now
    JOIN_CHANNELS: bool = True 
    AUTO_STAKING: bool = True
    PROTECTED_BALANCE: int = 100000 # minimum balance before staking

    AUTO_UPGRADE_FARM: bool = True # Not working for now
    MAX_UPGRADE_LEVEL: int = 6 # Not working for now


settings = Settings()
