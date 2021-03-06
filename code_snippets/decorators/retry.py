def retry(tries, delay=1, factor=2):

    import time
    import math
    import functools

    if factor <= 1:
        raise ValueError("back off must be greater than 1")

    tries = math.floor(tries)
    if tries < 0:
        raise ValueError("tries must be 0 or greater")

    if delay <= 0:
        raise ValueError("delay must be greater than 0")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _tries, _delay = tries, delay
            _tries += 1  # ensure we call func at least once
            while _tries > 0:
                try:
                    ret = func(*args, **kwargs)
                    return ret
                except Exception as e:
                    _tries -= 1
                    # retried enough and still fail? raise original exception
                    if _tries == 0:
                        raise e
                    time.sleep(_delay)
                    # wait longer after each failure
                    _delay *= factor

        return wrapper

    return decorator
