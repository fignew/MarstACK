import logging
from datetime import datetime
import pytz
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/prod/api/v1/setB2500Report")
async def set_b2500_report(request: Request):
    """
    Endpoint to emulate /prod/api/v1/setB2500Report
    Returns a simple JSON response {"code":1,"msg":"ok"}
    """
    # Log all query parameters
    params = dict(request.query_params)
    logger.info(f"GET /prod/api/v1/setB2500Report - Query params: {params}")

    return JSONResponse(content={"code": 1, "msg": "ok"})


@app.get("/app/neng/getDateInfoeu.php", response_class=PlainTextResponse)
async def get_date_info(request: Request):
    """
    Endpoint to emulate /app/neng/getDateInfoeu.php
    Returns the current date in the format _YYYY_MM_DD_HH_MM_SS_04_0_0_0
    I don't know what the 04 represents but it seems to be static.
    """
    # Log all query parameters
    params = dict(request.query_params)
    logger.info(f"GET /app/neng/getDateInfoeu.php - Query params: {params}")

    # Get current date in UTC and format it
    now = datetime.now(pytz.utc)

    # Format: _YYYY_MM_DD_HH_MM_SS_04_0_0_0
    formatted_date = f"_{now.year}_{now.month:02d}_{now.day:02d}_{now.hour:02d}_{now.minute:02d}_{now.second:02d}_04_0_0_0"

    return formatted_date


@app.post("/app/Solar/puterrinfo.php", response_class=PlainTextResponse)
async def put_err_info(request: Request):
    """
    Endpoint to emulate POST /app/Solar/puterrinfo.php
    Returns a simple text response "_1"
    """
    # Get the request body
    body = await request.body()
    body_str = body.decode("utf-8")

    # Log the request body
    logger.info(f"POST /app/Solar/puterrinfo.php - Request body: {body_str}")

    return "_1"


@app.get("/app/Solar/puterrinfo.php", response_class=PlainTextResponse)
async def get_err_info(request: Request):
    """
    Endpoint to emulate GET /app/Solar/puterrinfo.php
    Returns a simple text response "_2"
    """
    # Get the request body
    body = await request.body()
    body_str = body.decode("utf-8")

    # Log the request body
    logger.info(f"GET /app/Solar/puterrinfo.php - Request body: {body_str}")

    return "_2"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
