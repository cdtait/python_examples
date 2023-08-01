class MyCustomException(Exception):
    pass

def ensure_key_in_dict(key: str):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            if key not in kwargs:
                raise MyCustomException(f"{key} is required")
            original_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator

# Usage of the decorator
@ensure_key_in_dict("VAR1")
class MyClass:
    def __init__(self, **kwargs):
        self.var1 = kwargs.get("VAR1")
        self.var2 = kwargs.get("VAR2")

# Example usage
try:
    obj = MyClass(VAR2="Value of VAR2", VAR3="Value of VAR3")
    print("Object created successfully.")
except MyCustomException as e:
    print("Caught exception:", e)


class MyCustomException(Exception):
    pass

def is_required(key: str):
    def decorator(func):
        def wrapper(environment: dict, *args, **kwargs):
            if key not in environment:
                raise MyCustomException(f"{key} is required")
            return func(environment, *args, **kwargs)
        return wrapper
    return decorator

# Usage of the decorator
@is_required("VAR1")
def some_function(environment: dict):
    # Your function logic here
    return environment["VAR1"]

# Example usage
try:
    env_vars = {"VAR2": "Value of VAR2", "VAR3": "Value of VAR3"}
    result = some_function(env_vars)
    print("Result:", result)
except MyCustomException as e:
    print("Caught exception:", e)

