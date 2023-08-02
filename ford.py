# File ist versioned here:
# https://github.com/kwmiebach/ford

# Docs for decorators:
# https://www.saltycrane.com/blog/2010/03/simple-python-decorator-examples/


# Set this to False to raise an exception when
# a flow or task decorator is still used.
GRACE_PERIOD = True


task_runners = lambda: 0
task_runners.SequentialTaskRunner = "SequentialTaskRunner"

def flow(name="flow", task_runner=None):

    global GRACE_PERIOD
    if not GRACE_PERIOD:
        import pudb; pudb.set_trace()
        raise Exception("Phasing out prefect. Please remove the @flow decorators.")

    def decorating(decorated_function):
        from functools import wraps

        @wraps(decorated_function)
        def return_function(*args, **kwargs):
            print(f"START Flow '{name}' ...")
            result = decorated_function(*args, **kwargs)
            # print(f"DONE Flow '{name}',")
            return result

        return return_function

    return decorating


def task(name="task"):

    global GRACE_PERIOD
    if not GRACE_PERIOD:
        import pudb; pudb.set_trace()
        raise Exception("Phasing out prefect. Please remove the @task decorators.")

    def decorating(decorated_function):
        from functools import wraps

        @wraps(decorated_function)
        def return_function(*args, **kwargs):
            print(f"START Task '{name}' ...")
            result = decorated_function(*args, **kwargs)
            # print(f"DONE Task '{name}',")
            return result

        return return_function

    return decorating


def random_kebap_word(segments=2):
    # a helper for logging if you rely on prefects random words
    consonants = [
        'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'
    ]
    vowels = ['a','e','i','o','u','y']
    # Function to generate a wordpart.
    def syl():
        from random import choice as any
        return any(consonants) + any(vowels)
    def wrd():
        return syl() + syl()
    return '-'.join([wrd() for i in range(segments)])

def _info(msg):
    print(f"INFO: {msg}")


def _error(msg):
    print(f"ERROR: {msg}")


def get_run_logger():
    logger = lambda: 0
    logger.info = _info
    logger.error = _error
    return logger
