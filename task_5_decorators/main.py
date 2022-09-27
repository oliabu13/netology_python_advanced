import datetime

def decorator(path):
    def decor(some_function):
        def new_function(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = some_function(*args, **kwargs)
            with open(f'{path}logs.txt', 'a') as w_file:
                w_file.write(f'Имя функции: {some_function.__name__}\n'
                           f'Дата и время вызова: {start_time}\n'
                           f'Аргументы функции: {args} {kwargs}\n'
                           f'Результат функции: {result}\n')
            return result
        return new_function
    return decor





