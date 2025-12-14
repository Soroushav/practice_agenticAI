import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class PushToolInput(BaseModel):
    """Input schema for PushTool."""
    message: str = Field(description="Messsage to sent to the user")
class PushTool(BaseTool):
    name: str = "Send Push Notification"
    description: str = (
        "This tool is used to sent push notification to user."
    )
    args_schema: Type[BaseModel] = PushToolInput

    def _run(self, message: str) -> str:
        # Implementation goes here
        PUSHOVER_USER = os.getenv('PUSHOVER_USER')
        PUSHOVER_TOKEN = os.getenv('PUSHOVER_TOKEN')
        pushover_url = 'https://api.pushover.net/1/messages.json'

        payload = {
            "user": PUSHOVER_USER,
            "token": PUSHOVER_TOKEN,
            "message": message
        }
        requests.post(pushover_url, data=payload)
        return '{"notification": "ok"}'