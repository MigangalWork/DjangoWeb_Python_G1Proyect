# prototipo de aplicación Rentacar
# conexión con BBDD MySQL
# interfaz de usuario: consola

import exec_loop
import menu
import app_client
import app_admin
import database_create
import database_test_data


# ejecutar aplicación
def main():
    # reset de BD
    database_create.recreate_database__drop_exists()
    database_test_data.insert_test_data_in_database()

    # bucle de menú principal
    exec_loop.exec_loop(show_main_menu)


# mostrar menú principal
def show_main_menu():
    main_menu = (
        menu.Menu.Builder('Elija una opción:')
            .option('c', 'Entrar como cliente', app_client.enter)
            .option('a', 'Entrar como admin', app_admin.enter)
            .option('s', 'Salir', quit_app)
            .build()
    )

    return main_menu()


# terminar la aplicación
def quit_app():
    print()
    print('Ciao.')

    return exec_loop.QUIT_LOOP


if __name__ == '__main__':
    main()
