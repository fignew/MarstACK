import logging
from datetime import datetime
import pytz
import os
from fastapi import FastAPI, Request
from fastapi.responses import (
    JSONResponse,
    PlainTextResponse,
    HTMLResponse,
    FileResponse,
)
from fastapi.staticfiles import StaticFiles
import markdown

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure logging
logger = logging.getLogger("uvicorn.error")  # Use uvicorn's error logger


# Log unknown endpoints/methods as errors
@app.middleware("http")
async def log_error_middleware(request: Request, call_next):
    response = await call_next(request)
    if response.status_code in [404, 405]:
        logger.error(f'{response.status_code} ERROR - "{request.method} {request.url}"')
    return response


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")


@app.get("/", response_class=HTMLResponse)
async def marstack_homepage(request: Request):
    """
    Friendly Homepage for MarstACK
    """

    md_text = f"""
# MarstACK
![Logo](static/logo.png)
### Keep your solar battery online even when you're offline
---
*{
        "Success! You've correctly configured your DNS. Your batteries should now work offline."
        if request.url.hostname == "eu.hamedata.com"
        else "In order for your batteries to work offline you must configure your network's DNS. Check out the Wiki."
    }*

[MarstACK Github](https://www.github.com/fignew/MarstACK)

[MarstACK DNS Configuration Wiki](https://github.com/fignew/MarstACK/wiki)

[API Endpoint Documentation](/redoc)
"""
    html_content = markdown.markdown(md_text)
    return HTMLResponse(content=html_content)


@app.get("/prod/api/v1/setB2500Report")
async def set_b2500_report(request: Request):
    """
    Endpoint to emulate /prod/api/v1/setB2500Report

    Returns a simple JSON response {"code":1,"msg":"ok"}
    """
    # Log all query parameters
    params = dict(request.query_params)
    logger.debug(f"GET /prod/api/v1/setB2500Report - Query params: {params}")

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
    logger.debug(f"GET /app/neng/getDateInfoeu.php - Query params: {params}")

    # Get current date and format it
    # Return localtime or UTC if timezone is not set
    tz_name = os.getenv("APP_TIMEZONE")

    try:
        now = datetime.now(pytz.utc).astimezone(pytz.timezone(tz_name))
    except pytz.UnknownTimeZoneError:
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
    logger.debug(f"POST /app/Solar/puterrinfo.php - Request body: {body_str}")

    return "_1"


@app.get("/app/Solar/puterrinfo.php", response_class=PlainTextResponse)
async def get_err_info(request: Request):
    """
    Endpoint to emulate GET /app/Solar/puterrinfo.php

    Returns a simple text response "_2"
    Very rarely called
    """
    # Get the request body
    body = await request.body()
    body_str = body.decode("utf-8")

    # Log the request body
    logger.debug(f"GET /app/Solar/puterrinfo.php - Request body: {body_str}")

    return "_2"


@app.get("/ems/api/v1/getRealtimeSoc", response_class=JSONResponse)
async def get_realtime_soc(request: Request):
    """
    Endpoint to emulate GET /ems/api/v1/getRealtimeSoc

    Returns a simple JSON response:
    {"code":1,"show":0,"msg":"ok","data":{"soc":0,"time_no":0}}
    """
    # Log all query parameters
    params = dict(request.query_params)
    logger.debug(f"GET /ems/api/v1/getRealtimeSoc - Query params: {params}")

    return JSONResponse(
        content={"code": 1, "show": 0, "msg": "ok", "data": {"soc": 0, "time_no": 0}}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
