from reconfigure.items.bound import BoundData


def unquote(value):
    """Unquote a string.

    >>> unquote('"eth0"')
    'eth0'
    """
    if len(value) >= 2:
        first, last = value[0:1], value[-1:]
        if first == last and first in ("'", '"'):
            return value[1:-1]
    else:
        return value


def quote(value):
    """
    Force quoting a string.

    >>> quote('eth0')
    '"eth0"'
    """
    if '"' in value:
        return "'%s'" % value
    else:
        return '"%s"' % value


class WonderShaperData(BoundData):
    pass


class WonderShaperSectionData(BoundData):
    pass


WonderShaperData.bind_child('wondershaper',
                            lambda x: x.get('wondershaper'),
                            item_class=WonderShaperSectionData)

WonderShaperSectionData.bind_property('IFACE', 'IFACE',
                                      getter=unquote,
                                      setter=quote)

WonderShaperSectionData.bind_property('DSPEED', 'DSPEED',
                                      getter=unquote,
                                      setter=quote)

WonderShaperSectionData.bind_property('USPEED', 'USPEED',
                                      getter=unquote,
                                      setter=quote)
