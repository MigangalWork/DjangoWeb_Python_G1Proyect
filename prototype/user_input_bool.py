# peticiones de datos al usuario
# booleanos

# tiene que ser un módulo separado
# para evitar dependencia circular ente menu y user_input

from menu import Menu


# pedir un booleano al usuario
def ask_bool(what, default: bool = None):
    if default is None:
        what_string = what
    else:
        what_string = f'{what} (por defecto: {"sí" if default else "no"})'

    menu_builder = (
        Menu.Builder(what_string)
            .option('s', 'Sí.', lambda: True)
            .option('n', 'No.', lambda: False)
    )

    if default is not None:
        menu_builder.no_option(lambda: default)
    menu = menu_builder.build()

    return menu()


# test pedir booleano
def _test_ask_bool():
    while True:
        value = ask_bool('¿Es rápido?')
        print('Ha introducido:', type(value), value)


# test pedir booleano
# con valor por defecto
# True
def _test_ask_bool_with_default_true():
    while True:
        value = ask_bool('¿Es bonito?', True)
        print('Ha introducido:', type(value), value)


# test pedir booleano
# con valor por defecto
# False
def _test_ask_bool_with_default_false():
    while True:
        value = ask_bool('¿Es un agujero negro?', False)
        print('Ha introducido:', type(value), value)


# test
def _test():
    print('test')

    # _test_ask_bool()
    # _test_ask_bool_with_default_true()
    _test_ask_bool_with_default_false()


if __name__ == '__main__':
    _test()
