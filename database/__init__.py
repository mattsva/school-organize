# __init__.py for the database package
try:
    from .models import *
    from .crud import *
except ModuleNotFoundError as e:
    missing = e.name or "unknown module"
    raise RuntimeError(
        f'Error loading module "{missing}". Please install the package or check your import paths.'
    ) from e
