# Zoom LiveTrak L-12 with Linux

This is a repo documenting the random hiccups and hoops getting a Zoom LiveTrak L-12 running with Linux.

This is very WIP and not completely comprehensive.

## Scripts

### `l12pulse.py`

This script takes the raw inputs that PulseAudio creates and remaps them into separate inputs corresponding to the channels on the mixer. It _should_ be compatible with Python 2 or 3 (although my system uses Python 3.10). This could be done in raw shell script pretty easily, however I am lazy. Also due to my laziness you must put the serial number of your mixer in `SERIAL = ` in the script because I haven't programmed autodiscovery of that yet. It's easy to find by running `pactl list sources | grep device.serial` and looking for "ZOOM_Corporation_L-12...".
