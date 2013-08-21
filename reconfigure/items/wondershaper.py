from reconfigure.items.bound import BoundData


class WonderShaperData(BoundData):
    pass


class WonderShaperSectionData(BoundData):
    pass


WonderShaperData.bind_child('wondershaper',
                            lambda x: x.get('wondershaper'),
                            item_class=WonderShaperSectionData)

WonderShaperSectionData.bind_property('IFACE', 'IFACE')
WonderShaperSectionData.bind_property('DSPEED', 'DSPEED')
WonderShaperSectionData.bind_property('USPEED', 'USPEED')
