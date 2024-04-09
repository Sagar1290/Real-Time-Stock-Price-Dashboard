from fastapi import APIRouter, Query
from functions import get_data
from typing import List

import yfinance as yf
yf.pdr_override()

router = APIRouter()

@router.get("/api/stock_coordinates/")
async def stock_coordinates(symbol: str = Query(..., alias="symbol")):
    if symbol:
        stock_data = get_data(symbol).to_dict(orient="records")
        return {"data": stock_data}
    else:
        return {"error": "No stock symbols provided"}