import logging, sys
from typing import Any, Dict

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload : Dict [str, Any] = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "component": "api",
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return str(payload)

def configure_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.handlers.clear()
    root.addHandler(handler)