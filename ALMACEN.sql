create database Almacén
use Almacén
go

create table productos(
Id int primary key,
precio money, 
descripcion varchar(50)
);
go
create proc productos_datos
@Id int,
@precio money,
@descripcion varchar(50)
as
insert into productos(Id, precio, descripcion)values(@Id, @precio, @descripcion)
go

create proc eliminar_datos
@Id int
as
delete from productos where Id = @Id
go

create proc actualizar_datos
@Id int,
@precio money,
@descripcion varchar(50)
as
update productos set Id = @Id, precio = @precio, descripcion = @descripcion where Id = @Id

go

select * from productos
-- truncate table productos