from pydantic import BaseSettings


class WorkerSettings(BaseSettings):
    celery_broker_url: str
    celery_result_backend: str
