# funciones de menú

import user_input


# opción de menú
class MenuOption:
    def __init__(self, key, text, function):
        self.key = key
        self.text = text
        self.function = function


# menú
class Menu:
    # builder de menú
    class Builder:
        def __init__(self, menu_text):
            self.menu_text = menu_text
            self.options = []
            self.no_option_function = None

        # agregar opción de menú
        def option(self, key, text, function):
            option = MenuOption(key, text, function)

            self.options.append(option)

            return self

        # agregar función que se ejecuta cuando no se introduce ninguna opcion
        def no_option(self, function):
            self.no_option_function = function

            return self

        # crear menú
        def build(self):
            return Menu(self.menu_text, self.options, self.no_option_function)

    def __init__(self, menu_text, options, no_option_function):
        self.menu_text = menu_text
        self.options = options
        self.no_option_function = no_option_function

        self.map__key__option = {}
        for option in options:
            self.map__key__option[option.key] = option

    # mostrar menú
    def show_menu(self):
        print(self.menu_text)

        for option in self.options:
            print(f' {option.key}) {option.text}')

    # mostrar menú
    # pedir opción al usuario
    # ejecutar la opción seleccionada
    def __call__(self):
        # mostrar menú
        self.show_menu()

        # pedir opción al usuario
        selected_option = None
        while not selected_option:
            input_key = user_input.ask_string(None)

            if len(input_key) == 0:
                # no se introdujo ninguna opción
                if self.no_option_function:
                    # ejecutar función asociada a ninguna opción
                    return self.no_option_function()
                else:
                    # no hay función asociada a ninguna opción
                    # mostrar menú de nuevo
                    self.show_menu()
            elif input_key in self.map__key__option:
                selected_option = self.map__key__option[input_key]
            else:
                print('Ha introducido una opción no válida.')

        function = selected_option.function
        if function is not None:
            # ejecutar función asociada a opción de menú
            return function()
        else:
            # la opción de menú no tiene una función asociada
            return None


# línea de separación
SEPARATOR_LINE = '-' * 70


# imprimir línea de separación
def print_separator_line():
    print(SEPARATOR_LINE)


# test
def _test():
    def create_test_function(string):
        def print_string():
            print_separator_line()
            print(f'### {string} ###')

        return print_string

    quit_object = object()

    def quit_test():
        print_separator_line()
        print('ciao')
        return quit_object

    menu = Menu.Builder('Menú de test.') \
        .option('1', 'a', create_test_function('aaa')) \
        .option('2', 'b', create_test_function('bbb')) \
        .option('3', 'c', create_test_function('ccc')) \
        .option('q', 'quit', quit_test) \
        .no_option(create_test_function('...')) \
        .build()

    quit_check = None
    while quit_check != quit_object:
        print_separator_line()
        quit_check = menu()


if __name__ == '__main__':
    _test()
