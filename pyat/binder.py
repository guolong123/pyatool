from pyat.config import *


_func_map = dict()


def is_existed(func_name):
    return func_name in _func_map


def add(func_name, command, force=None):
    if not is_existed(func_name) or (is_existed(func_name) and force):
        _func_map[func_name] = command.split(' ')
        logger.info(TAG_BINDER, msg='function {} added'.format(func_name))
        return True
    logger.warn(TAG_BINDER, msg='function already existed', name=func_name)
    return False


def get(func_name):
    return _func_map.get(func_name)