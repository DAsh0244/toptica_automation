import logging as _logging

import time as _time

_formatter = _logging.Formatter('%(asctime)s - %(message)s')
# _logger = _logging.getLogger(__file__)
logger = _logging.getLogger('A')
# logger.setLevel(logging.DEBUG)  # defaults to logging.WARNING
_ch = _logging.StreamHandler()
_ch.setLevel(_logging.DEBUG)
_ch.setFormatter(_formatter)
logger.addHandler(_ch)
logger.setLevel(_logging.DEBUG)


def time_execution(desc=None, alert=None):
    """
    decorator to measure function execution time
    :param desc: string to be used inplace of function name
    :param alert: string to be displayed before function call
    :return: N/A
    """
    def decorator(method):
        def wrapper(*args, **kw):
            if alert:
                logger.debug('\n{}:'.format(alert.title()))
                # print('\n{}:'.format(alert.title()))
            t1 = _time.perf_counter()
            result = method(*args, **kw)
            t2 = _time.perf_counter()
            time_elapsed = _sec2time(t2 - t1)
            if desc:
                msg = '{} took {}'.format(desc, time_elapsed)
            else:
                msg = '"{}": Operation took {}'.format(method.__name__,  time_elapsed)
            logger.debug(msg)
            return result
        return wrapper
    return decorator


def _sec2time(sec, n_msec=5):
    """
    Convert seconds to "D days, HH:MM:SS.FFF"
    :param sec: number of seconds
    :param n_msec: number of milliseconds to use
    :return: string representing of time in human readable format
    """
    if hasattr(sec, '__len__'):
        return [_sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    d, h, m = int(d), int(h), int(m)
    if n_msec > 0:
        pattern = '{{:02d}}:{{:02d}}:{{:0{space}.{msec}f}}'.format(space=n_msec + 3, msec=n_msec)
        # pattern = '%%02d:%%02d:%%0%d.%df' %(n_msec+3, n_msec)
    else:
        pattern = '{:02d}:{:02d}:{:02d}'
        # pattern = r'%02d:%02d:%02d'
    if d == 0:
        # return pattern % (h, m, s)
        return pattern.format(h, m, s)
    return ('{:02d} days, ' + pattern).format(d, h, m, s)
