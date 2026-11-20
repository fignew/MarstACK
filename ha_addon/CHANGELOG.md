# Changelog

## 0.3.8

- New optional catch-all forwarder (`forward_url`): any request MarstACK
  does not serve itself is proxied to another URL on the same host, e.g.
  `https://127.0.0.1:443` to hand traffic like Ecowitt weather gateway
  webhooks to the Home Assistant web UI. Ecowitt gateways speak plain
  HTTP only (no TLS, and they ignore redirects), and Home Assistant
  cannot serve TLS and plain HTTP at the same time - so once HA hosts
  its own HTTPS, these devices cannot reach it directly and need a
  proxy on port 80. TLS to the target is used but
  its certificate is not verified (the target is normally addressed by
  loopback/IP, so the certificate name cannot match). Proxying is done
  by fastapi-proxy-lib (pinned to 0.3.x).

## 0.3.7

- Fixed startup crash in 0.3.6 (start.py missing from the app image)

## 0.3.6

- Fixed app options (timezone, redirect_url, log_level) not reaching the
  server; they are now read from Home Assistant's options file at startup
- Added this changelog

## 0.3.5

- First release of the Home Assistant app
- Optional redirect_url to send visitors to your Home Assistant web UI
  instead of the status page
- timezone setting so the battery's schedules follow your local clock
