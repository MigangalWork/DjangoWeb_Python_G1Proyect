# bucle de ejecución

import user_input

# constantes devueltas por funciones
QUIT_LOOP = 'quit'
CANCELLED = 'cancel'


# ejecutar bucle de ejecución
def exec_loop(function):
    while True:
        operation_return_value = function()

        if operation_return_value == QUIT_LOOP:
            break

        if operation_return_value == CANCELLED:
            print(' (cancelado)')
        else:
            user_input.request_enter_to_continue()
        print()


# cancelar operación
def cancel():
    return CANCELLED
