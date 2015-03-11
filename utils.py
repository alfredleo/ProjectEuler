import time

__author__ = 'Alfred'


def performance(inits=False):
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