from datetime import datetime

class Constant:
    LOGS_START_DATE: datetime = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
    LOGS_END_DATE:datetime = datetime(year=2025, month=3, day=1, hour=0, minute=0, second=0)
    NUMBER_OF_LOGS: int = 100000
    HTTP_METHODS: list[str] = ["GET","POST","PUT","DELETE"]
    API_ENDPOINTS: list[str] = ["/user","admi","login","/data","metrics"]

    HTTP_NORMAL_CODES: list[str] = ["200", "201", "204"]
    HTTP_ERROR_CODES: dict[str, list[str]] = {
        "server_errors": ["500", "502","503"],
        "client_errors": ["400", "401", "403", "404"],
        "timeout_errors": ["408", "504"]
    
    }

    NUMBER_OF_ANOMALY_INTERVALS: int = 5
    MIN_NUMBER_OF_ANOMALY_PER_INTERVAL: int = 500
    MAX_NUMBER_OF_ANOMALY_PER_INTERVAL: int = 1000
    NUMBER_OF_ANOMALY_IPS: int = 15
    LOGS_DATASET_FILE_NAME: str = "data/logs_dataset.csv"