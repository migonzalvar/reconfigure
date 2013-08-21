from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IniFileParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.wondershaper import WonderShaperData


class WonderShaperConfig(Reconfig):
    """
    ``/etc/conf.d/wondershaper.conf``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'builder': BoundBuilder(WonderShaperData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
