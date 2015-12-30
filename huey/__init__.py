__author__ = 'Charles Leifer'
__license__ = 'MIT'
__version__ = '0.9.0'

from huey.api import crontab
from huey.api import Huey

try:
    from huey.redis_backend import RedisHuey
except ImportError:
    class RedisHuey(object):
        def __init__(self, *args, **kwargs):
            raise RuntimeError('Error, "redis" is not installed. Install '
                               'using pip: "pip install redis"')
