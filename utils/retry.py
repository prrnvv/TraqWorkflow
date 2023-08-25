import time
from functools import wraps


def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_retries - 1:
                        time.sleep(delay)
                        print(f"Retrying---- Attempt {attempt + 1}/{max_retries}")
                    else:
                        raise e

        return wrapper

    return decorator
