## Flask SQLAlchemy

Este proyecto es un servicio para la administración de boletos de eventos que usa flask y mysql de manejador de base de datos usando SQLAlchemy.

### Instalación con docker-compose y Makefile

```
git clone https://github.com/jorgeminguer16/PruebaTecnica_AdmonBoletos.git
cd admon_boletos
Para ejecutar el código se utiliza el comando "python3 wsgi.py"
En otra terminal realizar las migraciones con el comando "flask db upgrade"

```
Antes de ejecutar la aplicación, debe configurar las siguientes variables de entorno de esta manera:
```
MYSQL_USER=root
MYSQL_ROOT_PASSWORD=root
MYSQL_PASSWORD=root
MYSQL_HOST=db
MYSQL_DATABASE=eventos_db
```

##### Requerimientos

* Python3 en su versión 3.7.9
* Mysql en su versión 8.0.31
