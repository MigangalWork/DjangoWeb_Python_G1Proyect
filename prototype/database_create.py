# creación de BD

import database


# TODO faltan las tablas y relaciones de cliente

# eliminar base de datos si existe
# crear base de datos de nuevo
def recreate_database__drop_exists():
    with database.DB.connect() as db:
        # info:
        # https://dba.stackexchange.com/questions/76788/create-a-mysql-database-with-charset-utf-8
        db.execute('''
drop database if exists rentacar;

create database rentacar
    character set utf8mb4
    collate utf8mb4_0900_ai_ci;

use rentacar;

create table car (
    id int not null auto_increment,
    model varchar(50) not null,
    number varchar(10) not null,
    km int not null,
    dtRegister datetime not null,
    primary key (id)
);

create table carAvailable (
    carId int not null,
    dtStart datetime not null,
    dtEnd datetime not null,
    foreign key (carId) references car(id)
        on delete cascade
        on update cascade
);

create table carRent (
    id int not null auto_increment,
    carId int not null,
    dtStart datetime not null,
    dtEnd datetime not null,
    status enum('reserved','confirmed','paid') not null,
    payAccount varchar(20),
    primary key (id),
    foreign key (carId) references car(id)
        on delete cascade
        on update cascade
);
        ''', multi=True)
