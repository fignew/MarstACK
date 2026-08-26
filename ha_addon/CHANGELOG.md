# Changelog

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
