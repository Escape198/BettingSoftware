from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from myapp.api import bets, events
from myapp.middlewares import setup_cors_middleware


app = FastAPI()
setup_cors_middleware(app)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Bet Maker API",
        version="1.0.0",
        description="This is the documentation for the Bet Maker API.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()


app.include_router(bets.router, prefix="/bets", tags=["bets"])
app.include_router(events.router, prefix="/events", tags=["events"])
