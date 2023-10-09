from typing import Optional
from datetime import datetime

from pydantic import BaseModel,Field


class PredictionResults(BaseModel):
    version: str
    predictions: Optional[int]
    actual_targets: Optional[int]

class BikeSharingDayDataInputs(BaseModel):
    """
    check latest documentation
    https://fastapi.tiangolo.com/tutorial/schema-extra-example/#__tabbed_1_1
    """
    instant: Optional[int] = Field()
    dteday: Optional[str] = Field()
    season: Optional[int] = Field()
    yr: Optional[int] = Field()
    mnth: Optional[int] = Field()
    holiday: Optional[int] = Field()
    weekday: Optional[int] = Field()
    workingday: Optional[int] = Field()
    weathersit: Optional[int] = Field()
    temp: Optional[float] = Field()
    atemp: Optional[float]= Field() #alias='normalized feeling temperature' in case we have a value named with spaces
    hum: Optional[float]= Field()
    windspeed: Optional[float] = Field()
    casual: Optional[int] = Field()
    registered: Optional[int] = Field()
    cnt: Optional[int] = Field()

    model_config = {
        "json_schema_extra": {
            "examples": [
                    {
                        'instant': 1000,
                        'dteday': '2024-02-01',
                        'season': 3,
                        'yr': 1,
                        'mnth': 10,
                        'holiday': 0,
                        'weekday': 3,
                        'workingday': 3,
                        'weathersit': 3,
                        'temp': 0.53,
                        'atemp': 0.44,
                        'hum': 0.21,
                        'windspeed': 0.1,
                        'casual': 300,
                        'registered': 700,
                        'cnt': 1000
                    }
                ]
            }
        }
    