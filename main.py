from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import stock_coordinates
from routers import calcEMA, calcATR
import uvicorn

def create_app():
    app = FastAPI()
    origins = ["http://localhost:3000", "http://localhost:8000", "http://localhost:8080"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(stock_coordinates.router)
    app.include_router(calcEMA.router)
    app.include_router(calcATR.router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run("main:create_app", host="localhost", port=8000, reload=True)
