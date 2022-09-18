import functools
import time


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = time.perf_counter()
        f_result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = round((end_time - start_time) * 1000, 2)
        return {
            'run_time': run_time,
            'result': f_result
        }
    return wrapper_decorator
