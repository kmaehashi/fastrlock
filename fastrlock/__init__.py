# this is a package

__version__ = "0.7"


class LockNotAcquired(Exception):
    """
    Exception raised when the lock was not acquired in non-blocking mode.
    """
