# MarstACK — Home Assistant app

Emulates the `eu.hamedata.com` cloud servers so Marstek balcony solar
batteries keep working without internet access, right on your Home
Assistant host.

## Configuration

| Option | Default | Description |
|---|---|---|
| `log_level` | `info` | Log verbosity: `error`, `info`, or `debug`. Use `debug` to see every request the battery makes (useful when something doesn't work). |
| `timezone` | `UTC` | IANA time zone name used for the date endpoint, e.g. `Europe/Berlin`. The battery uses this for its daily schedules, so set it to your local zone. |
| `redirect_url` | *(empty)* | Optional. When set, visiting `http://<your-ha-host>/` redirects to this URL instead of showing the MarstACK status page. Handy to point browsers at your Home Assistant web UI, e.g. `https://homeassistant.local:8123`. Leave empty to keep the status page. |

## Requirements

- **Port 80 must be free** on the Home Assistant host. The battery
  contacts the server on plain HTTP port 80, and this app shares the
  host network (`host_network`) to bind it directly.

  Since Home Assistant OS 2026.8, **new installations listen on port 80
  themselves**, which conflicts with this app. Move Home Assistant's own
  web port first: **Settings → System → Network → HTTP server port**
  (e.g. back to `8123`). Existing installs that already use 8123 are not
  affected. Disable other port-80 users too (e.g. the Nginx Proxy
  Manager add-on).

## DNS setup

The battery must be made to contact *this* server instead of the real
cloud. Configure your network's DNS so that
`eu.hamedata.com` resolves to your Home Assistant host's IP address.
See the [MarstACK Wiki](https://github.com/fignew/MarstACK/wiki) for
router-specific instructions.

## Verifying it works

Open `http://<your-ha-host>/` in a browser:

- Without `redirect_url`: you see the MarstACK status page.
- With `redirect_url` set: you are redirected to the configured URL.

The API endpoints under `/prod/`, `/app/`, and `/ems/` serve the battery;
watch the app log at `debug` level to see them being called.
