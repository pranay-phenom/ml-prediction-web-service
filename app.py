"""
Controller
"""
import os
import uvicorn

from fastapi import FastAPI

from src.utils.logging_util import Logger
from src.configurations.app_configs import AppConfigs
from src.domain.constants import SOCKET_HOST, PORT
from src.domain.request_response_schemas import BuildResponse
from src.routers import v1

tags_metadata = [
    {"name": "Build", "description": "Use this API to check project build number."},
    {
        "name": "Prediction Service",
        "description": "Prediction Service APIs",
        "externalDocs": {
            "description": "Project API Documentation",
            "url": "https://ml-prediction-web-service.herokuapp.com/redoc",
        },
    },
]

app = FastAPI(
    title="ML Prediction Web Service",
    description="This project is a sentence classifier trained on cooking section of StackExchange. Given a question it will suggest the appropriate label for the question."
    "<br /><br />"
    "Author - [***Pranay Chandekar***](https://www.linkedin.com/in/pranaychandekar/)",
    version="2.0.0",
    openapi_tags=tags_metadata,
    docs_url="/swagger/",
)

LOGGER = Logger.get_instance()
APP_CONFIGS = AppConfigs.get_instance()


@app.get("/", tags=["Build"], response_model=BuildResponse)
async def build():
    """
    Hit this API to get build details.

    :return: The build details
    """
    LOGGER.logger.info("Checking the service setup.\n")
    return {
        "service": "ml-prediction-web-service",
        "version": "2.0",
        "author": "Pranay Chandekar",
        "linkedIn": "https://www.linkedin.com/in/pranaychandekar/",
        "message": "The web service is up and running!",
    }

app.include_router(v1.router, prefix="/v1")

if __name__ == "__main__":
    LOGGER.logger.info("Starting the web service.")
    uvicorn.run(
        app,
        host=APP_CONFIGS.get_configuration(SOCKET_HOST),
        port=os.environ.get('PORT', '5000'),
    )
