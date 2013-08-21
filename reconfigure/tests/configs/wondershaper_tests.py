from reconfigure.configs import WonderShaperConfig
from base_test import BaseConfigTest


class WonderShaperConfigTest (BaseConfigTest):
    sources = {
        None: """[wondershaper]
IFACE="eth0"
DSPEED="2048"
USPEED="512"
"""
    }
    result = {
    "wondershaper": {
        "USPEED": "\"512\"",
        "IFACE": "\"eth0\"",
        "DSPEED": "\"2048\""
    }
}
    config = WonderShaperConfig


del BaseConfigTest
