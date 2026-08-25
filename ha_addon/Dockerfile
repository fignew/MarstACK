# Thin wrapper around the regular MarstACK image, built by Home Assistant
# from the contents of this directory only (files outside it, including
# symlinks, are not visible to the add-on build).
#
# The add-on shares the host network (see config.yaml), so the server has to
# bind port 80 itself. Binding a privileged port requires root.
FROM ghcr.io/fignew/marstack:latest

USER root

EXPOSE 80

CMD ["/bin/sh", "-c", "uvicorn main:app --log-level ${LOG_LEVEL} --host 0.0.0.0 --port 80"]
