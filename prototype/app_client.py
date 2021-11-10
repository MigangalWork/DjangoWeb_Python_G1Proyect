# opciones de cliente

import user_input
import user_input_bool
import clients
import vehicle_rents
import vehicles
import exec_loop
import menu

# cliente
client = None


# entrar como cliente
def enter():
    login()
    if client is None:
        return

    exec_loop.exec_loop(show_menu)


# mostrar menú
def show_menu():
    client_menu = (
        menu.Menu.Builder('Elija una opción:')
            .option('a', 'Alquilar un coche', rent_vehicle)
            .option('o', 'Logout', logout)
            .build()
    )

    return client_menu()


# login
def login():
    email = user_input.ask_string('email', clients.VALID_USER_EMAIL)
    password = user_input.ask_string('password', clients.VALID_USER_PASSWORD)

    global client
    client = clients.get_client_by_email_password(email, password)

    if client is None:
        print('No se encuentra este cliente o la contraseña es incorrecta.')

    else:
        print()
        print(f'Ha entrado como {client.name} (#{client.client_id}, {client.email}).')
        print()


# logout
def logout():
    global client

    print()
    # noinspection PyUnresolvedReferences
    print(f'Ciao, {client.name}.')

    client = None

    return exec_loop.QUIT_LOOP


# alquilar un vehículo
def rent_vehicle():
    rent = vehicle_rents.Rent()

    rent.datetime_start = user_input.ask_datetime('fecha comienzo', 'hora comienzo')
    rent.datetime_end = user_input.ask_datetime('fecha fin', 'hora fin')

    vehicle_rents.reserve_vehicle(rent)
    if rent.vehicle_id is None:
        print('No hay coches disponibles para esta franja.')
        return

    print('Disponemos de un vehículo para esta franja.')
    print(f'Vehículo: #{rent.vehicle_id}')
    print()

    print('Introduzca los datos de pago.')
    rent.pay_account = user_input.ask_string('número de cuenta')

    confirm_rent = user_input_bool.ask_bool('¿Confirmar el alquiler?')

    if not confirm_rent:
        print('El alquiler ha sido cancelado.')

    else:
        rented_vehicle = vehicle_rents.rent_vehicle(rent)

        if rented_vehicle is not None:
            print('El vehículo ha sido alquilado.')
            print('Éstos son los datos de su vehículo:')
            vehicles.print_rented_vehicle(rented_vehicle)

        else:
            print(
                'Se ha producido un error.\n'
                'No se ha podido alquilar el vehículo.')
