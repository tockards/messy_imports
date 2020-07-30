from future import standard_library
standard_library.install_aliases()
import future

if future.utils.PY2:
    from . import bye as message_bus_broker
else:
    from . import bye3 as message_bus_broker