from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str
    user: str
    password: str
    name: str
    debug: bool = True

    @property
    def url(self):
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}/{self.name}"

    class Config:
        env_prefix = "db_"
