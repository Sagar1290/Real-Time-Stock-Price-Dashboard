from fastapi import APIRouter
from models.stock_coord_models import StockCoordinateDetails
from functions import get_data
from ta.volatility import AverageTrueRange

router = APIRouter()

@router.post("/api/calcATR")
async def calculate_atr(item: StockCoordinateDetails):
    data = get_data(item)
    atr = AverageTrueRange(high=data['High'], low=data['Low'], close=data['Close'], window=14)
    data['ATR'] = atr.average_true_range()
    return {"data": data.to_dict(orient="records")}
