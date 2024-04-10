from fastapi import APIRouter
from models.stock_coord_models import StockCoordinateDetails
from functions import get_data

router = APIRouter()

@router.post("/api/calcEMA")
async def calculate_ema(item: StockCoordinateDetails):
    data = get_data(item)
    data['EMA'] = data['Close'].ewm(span=14, adjust=False).mean()
    return {"data": data.to_dict(orient="records")}
