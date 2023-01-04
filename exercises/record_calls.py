from dataclasses import dataclass
from functools import update_wrapper, wraps

import wrapt


@dataclass
class Call:
    args: tuple
    kwargs: dict


def record_calls(func):
    """Record calls to the given function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


#class decorator
class record_calls_class(wrapt.ObjectProxy):
    """Record calls to the given function."""

    def __init__(self, func):
        super().__init__(func)
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.__wrapped__(*args, **kwargs)


@record_calls_class
def greet(name="world"):
    """Greet someone by their name."""
    print(f"{name}")
    return
