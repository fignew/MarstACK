# MarstACK Home Assistant app

Runs the MarstACK server on your Home Assistant host so your Marstek
battery keeps working when the cloud is unreachable.

## Configuration

| Option | Default | Description |
|---|---|---|
| `log_level` | `info` | Log verbosity: `error`, `info`, or `debug`. Use `debug` if something doesn't work; you'll see every request the battery sends. |
| `timezone` | `UTC` | IANA name like `Europe/Berlin`. The battery builds its daily schedules from the time this endpoint reports, so set your local zone or your schedules will be off. |
| `redirect_url` | *(empty)* | If set (for example to `https://homeassistant.local:8123`), anyone opening `http://<your-ha-host>/` lands on that address instead of the MarstACK status page. Leave empty for the status page. Mind the port: newer installs may use 80, older ones 8123, reverse proxies something else entirely, so use whatever URL you actually reach Home Assistant at. |

## Before you install

This app needs port 80 on the Home Assistant host, because that's the
port the battery contacts. Two things commonly occupy it:

- Since Home Assistant OS 2026.8, fresh installs listen on port 80 for
  their own web UI. Move that first: Settings → System → Network → HTTP
  server port, and pick something like the old default 8123. Existing
  installs already on 8123 don't need to change anything.
- Other add-ons can also hold port 80, most often the Nginx Proxy
  Manager add-on. Disable those too.

## DNS setup

Your battery needs to reach this server when it looks up
eu.hamedata.com. Point that hostname at your Home Assistant host's IP
in your router's DNS. The
[MarstACK Wiki](https://github.com/fignew/MarstACK/wiki) has
instructions for common routers.

## Checking that it works

Open `http://<your-ha-host>/` in a browser. You should either see the
MarstACK status page or land on your redirect target, depending on how
you configured `redirect_url`.

The battery's requests show up in the app log; switch log_level to
`debug` to watch them come in.
