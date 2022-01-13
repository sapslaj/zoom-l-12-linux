#!/bin/python
from __future__ import print_function
import os

# TODO: autodiscover this
SERIAL = "ZOOM_Corporation_L-12_8283FFFFFFFFFFFF21DFFFFFFFFFFFFF"

PA_INPUTS = [
    "front-left",
    "front-right",
    "rear-left",
    "rear-right",
    "front-center",
    "lfe",
    "side-left",
    "side-right",
    "aux0",
    "aux1",
    "aux2",
    "aux3",
    "aux4",
    "aux5",
]


def pa_remap(name, **kwargs):
    kwargs["source_name"] = name
    kwargs["source_properties"] = "device.description='{0}'".format(name)
    kwargs["master"] = "alsa_input.usb-{0}-00.multichannel-input".format(SERIAL)
    cmd = "pactl load-module module-remap-source"
    for key, value in kwargs.items():
        cmd += ' {0}="{1}"'.format(key, value)
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    # Mono inputs
    for i in range(8):
        pa_remap(
            "L-12-Channel-{0}".format(str(i + 1)),
            master_channel_map=PA_INPUTS[i],
            channel_map="mono",
        )
    # Stereo inputs
    for lr in zip(*[iter(range(8, 12))] * 2):
        pa_remap(
            "L-12-Channel-{0}/{1}".format(*[i + 1 for i in lr]),
            master_channel_map=",".join(PA_INPUTS[lr[0] : lr[1] + 1]),
            channel_map="front-right,front-left",
        )
    # Master
    pa_remap(
        "L-12-Master",
        master_channel_map=",".join(PA_INPUTS[-2:]),
        channel_map="front-right,front-left",
    )
