# alquileres de vehículos

import database
import vehicles


# alquiler de vehículo
class Rent:
    def __init__(
            self,
            rent_id=None,
            vehicle_id=None,
            client_id=None,
            datetime_start=None,
            datetime_end=None,
            pay_account=None
    ):
        self.rent_id = rent_id
        self.vehicle_id = vehicle_id
        self.client_id = client_id
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.pay_account = pay_account


# reservar un vehículo
# antes del pago
def reserve_vehicle(rent: Rent):
    with database.connect_rentacar_database() as db:
        # buscar vehículo disponible

        db.execute(
            '''
select a.carId, a.dtEnd from carAvailable a
join car c on (a.carId = c.id)
where a.dtStart <= %s and a.dtEnd >= %s
order by c.km
limit 1
'''
        )
        row = db.cursor.fetchone()

        if row is None:
            # no hay vehículo disponible
            rent.vehicle_id = None
            return

        rent.vehicle_id, \
        datetime_available_end \
            = row

        # reservar vehículo

        # insertar alquiler
        db.execute(
            '''
insert into carRent (carId, dtStart, dtEnd, status)
values (%s, %s, %s, 'reserved');
''',
            rent.vehicle_id,
            rent.datetime_start,
            rent.datetime_end
        )

        rent.rent_id = db.cursor.lastrowid

        if rent.rent_id is None:
            raise ValueError('No se pudo insertar alquiler.')

        # dividir intervalo de disponibilidad en dos,
        # con el intervalo de alquiler en medio
        db.execute(
            '''
update carAvailable
set dtEnd = %s
where carId = %s and dtEnd = %s;

insert into carAvailable (carId, dtStart, dtEnd)
values (%s, %s, %s)
''',
            # params de update
            rent.datetime_start,
            rent.vehicle_id,
            datetime_available_end,
            # params de insert
            rent.vehicle_id,
            rent.datetime_end,
            datetime_available_end
        )

        if db.cursor.rowcount != 1:
            raise ValueError('No se pudo actualizar disponibilidad.')


# realizar alquiler de un vehículo
# devuelve el vehículo alquilado
def rent_vehicle(rent: Rent):
    if not rent.pay_account:
        raise ValueError('Falta la cuenta de pago.')

    with database.connect_rentacar_database() as db:
        db.execute(
            '''
update carRent
set status = 'confirmed', payAccount = %s
where id = %s
''',
            rent.pay_account,
            rent.rent_id
        )

        return vehicles.get_vehicle(rent.vehicle_id)


# cancelar alquiler de un vehículo
def cancel_vehicle_rent(rent: Rent):
    with database.connect_rentacar_database() as db:
        # eliminar alquiler

        db.execute(
            '''
delete from carRent
where id = %s
''',
            rent.rent_id
        )

        # restaurar intervalo de disponibilidad

        db.execute(
            '''
select dtEnd
from carAvailable
where carId = %s and dtStart = %s
''',
            rent.vehicle_id,
            rent.datetime_end
        )
        row = db.cursor.fetchone()
        datetime_available_end, \
            = row

        db.execute(
            '''
delete from carAvailable
where carId = %s and dtStart = %s
''',
            rent.vehicle_id,
            rent.datetime_end
        )
        db.execute(
            '''
update carAvailable
set dtEnd = %s
where carId = %s and dtEnd = %s
''',
            datetime_available_end,
            rent.vehicle_id,
            rent.datetime_start
        )
