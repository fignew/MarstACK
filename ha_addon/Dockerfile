# Thin wrapper around the regular MarstACK image, built by Home Assistant
# from the contents of this directory only (files outside it, including
# symlinks, are not visible to the add-on build).
#
# The add-on shares the host network (see config.yaml), so the server has to
# bind port 80 itself. Binding a privileged port requires root.
FROM ghcr.io/fignew/marstack:latest

COPY start.py /code/app/start.py

USER root

EXPOSE 80

# The Supervisor passes app options via /data/options.json, not env vars.
# start.py maps them to the env vars the app reads, then execs uvicorn so
# it runs as PID 1 and receives signals directly.
CMD ["python3", "/code/app/start.py"]
