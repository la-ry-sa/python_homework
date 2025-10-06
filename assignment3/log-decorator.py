import logging

# one-time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./assignment3/decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        positional = args if args else "none"
        keyword = kwargs if kwargs else "none"
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
            "-----------------------"
        )
        logger.log(logging.INFO, log_message)
        return result
    return wrapper

@logger_decorator
def hello():
    print("Hello, Decorators!")

@logger_decorator
def honest(*args):
    return True

@logger_decorator
def mind_blowing(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello()  
    honest(1, 2, 3, 4) 
    mind_blowing(a=1, b=2, c="Dusty the Cat") 