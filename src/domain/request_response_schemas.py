"""
Request Schemas
"""
from pydantic import BaseModel, Field


class BuildResponse(BaseModel):
    """
    Build Response Schema
    """
    service: str = Field(..., example="ml-prediction-web-service")
    version: str = Field(..., example="2.0.0")
    author: str = Field(..., example="Pranay Chandekar")
    linkedIn: str = Field(..., example="https://www.linkedin.com/in/pranaychandekar/")
    message: str = Field(..., example="The web service is up and running!")


class PredictionServiceRequest(BaseModel):
    """
    Prediction Service Request Schema
    """

    source: str = Field(..., min_length=1, example="openapi")
    text: str = Field(..., min_length=1, example="Which plastic wrap is okay for oven use?")


class PredictionServiceResponse(BaseModel):
    """
    Prediction Service Response Schema
    """

    label: str = Field(..., example="baking")
    confidence: float = Field(..., example=98.86)
