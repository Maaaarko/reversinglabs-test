from re import S
from time import sleep, time


def cache(function):
    """
    A decorator that caches the result of a function.
    The result is cached for 10 subsequent calls or 5 minutes - whichever comes first.
    """
    import time
    from collections import OrderedDict

    TTL = 5 * 60
    MAX_CALLS = 10
    cache = OrderedDict() # in Python 3.7+, it's not needed to use OrderedDict

    def wrapper(*args, **kwargs):
        key = (function.__name__,) + (*args,) + tuple([(k,v) for k, v in kwargs.items()])
        if key in cache and time.time() < cache[key]['time']:
            result = cache[key]["result"]
            cache[key]["calls"] += 1
        else:
            result = function(*args, **kwargs)
            cache[key] = {"result": result, "time": time.time() + TTL, "calls": 1}
        
        if cache[key]["calls"] == MAX_CALLS:
            del cache[key]
        
        while True and len(cache) > 0:
            oldest = list(cache.keys())[0]
            if time.time() > cache[oldest]["time"]:
                del cache[oldest]
            else:
                break

        return result
    return wrapper
