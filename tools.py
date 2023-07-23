import os
import datetime


def write_log(path, name_function, arg, res):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(
            f'\n[{datetime.datetime.now()}] Имя функции: {name_function}; аргументы: {arg}; возвращаемое значение: {res}')


def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            write_log(path, old_function.__name__, f'{args} и {kwargs}', result)
            return result

        return new_function

    return _logger
