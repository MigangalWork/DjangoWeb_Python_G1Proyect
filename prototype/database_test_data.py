# contenido de BD de prueba

import vehicles
import datetime


# insertar datos de prueba en BD
def insert_test_data_in_database():
    test_vehicle = vehicles.Vehicle(
        model='Alfa',
        number='1111 AAA',
        km=0,
        datetime_register=datetime.datetime.now()
    )
    vehicles.create_vehicle(test_vehicle)

    test_vehicle = vehicles.Vehicle(
        model='Beta',
        number='2222 BBB',
        km=0,
        datetime_register=datetime.datetime.now()
    )
    vehicles.create_vehicle(test_vehicle)

    test_vehicle = vehicles.Vehicle(
        model='Gamma',
        number='3333 CCC',
        km=0,
        datetime_register=datetime.datetime.now()
    )
    vehicles.create_vehicle(test_vehicle)
