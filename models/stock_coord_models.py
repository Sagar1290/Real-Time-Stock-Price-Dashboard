from pydantic import BaseModel


class StockCoordinateDetails(BaseModel):
    name: str
    start_date: str
    end_date: str
    period: str = "3mon"
