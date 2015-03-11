import time

__author__ = 'Alfred'


def p(inits=False):
    """
    Performance measerement tool
    :param inits: init start time on first call
    """
    if inits or 'start' not in globals():
        global start
        start = in_millis(time.time())
    else:
        end = in_millis(time.time())
        print end - start
        start = end


def in_millis(t):
    return int(round(t * 1000))


def calculateRunTime(function, *args):
    """ Alternative approach to test runtime.
    Run a function and return the run time and the result of the function
    if the function requires arguments, those can be passed in too"""
    startTime = time.time()
    result = function(*args)
    return time.time() - startTime, result
