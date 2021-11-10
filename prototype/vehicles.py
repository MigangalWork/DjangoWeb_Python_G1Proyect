# vehículos

import database
import datetime


# vehículo
class Vehicle:
    def __init__(
            self,
            vehicle_id=None,
            model=None,
            number=None,
            km=None,
            datetime_register=None
    ):
        self.vehicle_id = vehicle_id
        self.model = model
        self.number = number
        self.km = km
        self.datetime_register = datetime_register

    def __str__(self):
        return (
            f'Vehicle ('
            f'id = {self.vehicle_id}, '
            f'model = {self.model}, '
            f'number = {self.number}, '
            f'km = {self.km}, '
            f'dt register = {self.datetime_register}'
            f')'
        )

    def __repr__(self):
        return self.__str__()


# crear un vehículo
def create_vehicle(vehicle: Vehicle):
    with database.connect_rentacar_database() as db:
        db.execute(
            '''
insert into car (model, number, km, dtRegister)
values (%s, %s, %s, %s)
''',
            vehicle.model,
            vehicle.number,
            vehicle.km,
            vehicle.datetime_register
        )

        vehicle_id = db.cursor.lastrowid

        # se sustrae un segundo para evitar overflow
        datetime_max = (
                datetime.datetime.max
                - datetime.timedelta(seconds=1)
        )

        db.execute(
            '''
insert into carAvailable (carId, dtStart, dtEnd)
values (%s, %s, %s)
''',
            vehicle_id,
            vehicle.datetime_register,
            datetime_max
        )

        if db.cursor.rowcount == 1:
            return vehicle_id
        else:
            raise ValueError('Could not create vehicle.')


# obtener un vehículo por id
def get_vehicle(vehicle_id):
    with database.connect_rentacar_database() as db:
        db.execute(
            '''
select model, number, km, dtRegister
from car
where id = %s
''',
            vehicle_id
        )

        row = db.cursor.fetchone()

        if row is None:
            # no se encuentra el vehículo
            return None

        model, number, km, datetime_register = row

        return Vehicle(
            vehicle_id=vehicle_id,
            model=model,
            number=number,
            km=int(km),
            datetime_register=datetime_register
        )


# mostrar datos de vehículo alquilado
def print_rented_vehicle(rented_vehicle):
    print(rented_vehicle)
