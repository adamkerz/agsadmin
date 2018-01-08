from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from enum import Enum

class ServiceType(Enum):
    MAP_SERVER = "MapServer"
    GP_SERVER = "GpServer"
    IMAGE_SERVER = "ImageServer"
    GEOCODE_SERVER = "GeocodeServer"

    @staticmethod
    def _get_proxy(service_type):
        from .MapServer import MapServer
        from .GpServer import GpServer
        from .ImageServer import ImageServer
        from .GeocodeServer import GeocodeServer

        _type_map = {
            ServiceType.MAP_SERVER: MapServer,
            ServiceType.GP_SERVER: GpServer,
            ServiceType.IMAGE_SERVER: ImageServer,
            ServiceType.GEOCODE_SERVER: GeocodeServer
        }

        service_type = ServiceType(service_type)

        return _type_map[service_type]