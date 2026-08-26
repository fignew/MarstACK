"""Read Home Assistant app options and exec the server.

The Supervisor writes user options to /data/options.json; it does not
set environment variables. This script maps them to the env vars the
MarstACK app understands and hands over to uvicorn.
"""
import json
import os

with open("/data/options.json") as f:
    options = json.load(f)

os.environ["LOG_LEVEL"] = options.get("log_level", "info")
os.environ["TIMEZONE"] = options.get("timezone", "UTC")
if options.get("redirect_url"):
    os.environ["REDIRECT_URL"] = options["redirect_url"]

port = options.get("port", 80)
os.execvp(
    "uvicorn",
    [
        "uvicorn", "main:app",
        "--log-level", os.environ["LOG_LEVEL"],
        "--host", "0.0.0.0",
        "--port", str(port),
    ],
)
