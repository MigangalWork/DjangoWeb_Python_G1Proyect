# peticiones de datos al usuario

import datetime


# error: input de usuario no válido
class InvalidUserInput(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    # mostrar mensaje de error
    def print_message(self):
        print(self.message)


# pedir una cadena de entrada al usuario
def _ask_input(what):
    if what:
        return input(' {} > '.format(what)).strip()
    else:
        return input(' > ').strip()


# pedir que el usuario pulse intro para continuar
def request_enter_to_continue():
    input(' --- pulse intro para continuar ---')


# pedir una cadena al usuario
def ask_string(what, default=None):
    if default is None:
        what_string = what
    else:
        what_string = f'{what} (por defecto: {default})'

    input_string = _ask_input(what_string)

    if default is not None and len(input_string) == 0:
        return default

    return input_string


# pedir un entero positivo al usuario
def ask_positive_integer(what, default=None, default_string=None):
    if default is None:
        what_string = what
    else:
        if default_string is None:
            default_string = str(default)
        what_string = f'{what} (por defecto: {default_string})'

    while True:
        try:
            input_string = _ask_input(what_string)

            if default is not None and len(input_string) == 0:
                return default

            try:
                value = int(input_string)
            except ValueError:
                raise InvalidUserInput('Debe introducir un número entero.')

            if value < 0:
                raise InvalidUserInput('Debe introducir un número mayor o igual que 0.')

            return value

        except InvalidUserInput as error:
            error.print_message()


# pedir un float positivo al usuario
def ask_positive_float(what, default=None, default_string=None):
    if default is None:
        what_string = what
    else:
        if default_string is None:
            default_string = str(default)
        what_string = f'{what} (por defecto: {default_string})'

    while True:
        try:
            input_string = _ask_input(what_string)

            if default is not None and len(input_string) == 0:
                return default

            try:
                value = float(input_string)
            except ValueError:
                raise InvalidUserInput('Debe introducir un número.')

            if value < 0:
                raise InvalidUserInput('Debe introducir un número mayor o igual que 0.')

            return value

        except InvalidUserInput as error:
            error.print_message()


# pedir una fecha y hora al usuario
def ask_datetime(what_date, what_time):
    while True:
        input_date_string = ask_string(what_date)
        try:
            input_date = datetime.datetime.strptime(
                input_date_string, '%Y-%m-%d')
            break
        except ValueError:
            print('Debe introducir año-mes-día.')

    while True:
        input_time_string = ask_string(what_time)
        try:
            input_time = datetime.datetime.strptime(
                input_time_string, '%H:%M')
            break
        except ValueError:
            print('Debe introducir hora:minuto.')

    return datetime.datetime(
        input_date.year,
        input_date.month,
        input_date.day,
        input_time.hour,
        input_time.minute
    )


# test pedir cadena
def _test_ask_string():
    while True:
        value = ask_string('nombre')
        print('Ha introducido:', type(value), f'\'{value}\'')


# test pedir cadena
# con valor por defecto
def _test_ask_string_with_default():
    while True:
        value = ask_string('planeta', 'B 612')
        print('Ha introducido:', type(value), f'\'{value}\'')


# test pedir entero positivo
def _test_ask_positive_integer():
    while True:
        value = ask_positive_integer('galletas')
        print('Ha introducido:', type(value), value)


# test pedir entero positivo
# con valor por defecto
def _test_ask_positive_integer_with_default():
    while True:
        value = ask_positive_integer('caballos', 3)
        print('Ha introducido:', type(value), value)


# test pedir entero positivo
# con valor por defecto
# con cadena de valor por defecto
def _test_ask_positive_integer_with_default_string():
    while True:
        default = 42
        value = ask_positive_integer('peso', default, str(default) + ' gramos')
        print('Ha introducido:', type(value), value)


# test pedir float positivo
def _test_ask_positive_float():
    while True:
        value = ask_positive_float('leche')
        print('Ha introducido:', type(value), value)


# test pedir float positivo
# con valor por defecto
def _test_ask_positive_float_with_default():
    while True:
        value = ask_positive_float('fabulosidad', 3.1416)
        print('Ha introducido:', type(value), value)


# test pedir float positivo
# con valor por defecto
# con cadena de valor por defecto
def _test_ask_positive_float_with_default_string():
    while True:
        default = 3.5
        value = ask_positive_float('tamaño', default, str(default) + ' pulgadas')
        print('Ha introducido:', type(value), value)


# test pedir fecha y hora
def _test_ask_datetime():
    while True:
        value = ask_datetime('fecha nacimiento', 'hora nacimiento')
        print('Ha introducido:', type(value), value.strftime('%Y-%m-%d %H:%M'))


# test
def _test():
    print('test')

    # _test_ask_string()
    # _test_ask_string_with_default()
    # _test_ask_positive_integer()
    # _test_ask_positive_integer_with_default()
    # _test_ask_positive_integer_with_default_string()
    # _test_ask_positive_float()
    # _test_ask_positive_float_with_default()
    # _test_ask_positive_float_with_default_string()
    _test_ask_datetime()


if __name__ == '__main__':
    _test()
