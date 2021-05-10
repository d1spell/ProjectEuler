import time


def execution_time(func):
    def wrapper():
        time_start = time.monotonic()
        return f'{func()} \nExecution time =  {time.monotonic() - time_start}'
    return wrapper
