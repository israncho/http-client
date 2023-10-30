# http-client
Implementacion de un cliente HTTP con python.

## Requerimientos

Es necesario tener `docker` instalado, para verificar esto podemos ejecutar
el siguiente comando:

```shell
docker --version
```

Y en nuestro caso este comando tiene la siguiente salida:

```shell
Docker version 24.0.7, build afdd53b
```

## Uso

Proporcionamos shell scripts para facilitar el uso. Para
construir la imagen de Docker:

```shell
./build.sh
```

Para entrar a la imagen de Docker:

```shell
./enter_container.sh
```

Y tambien el script `tests.sh` que se agrega a la imagen, para
ejecutar de forma sencilla el programa con algunos ejemplos como:

```shell
python3 /ruta/a/http_client.py cirrus.dcaa.unam.mx GET / 1 identity close
```

El cual tendra la salida:

```shell
python3 src/http_client.py cirrus.dcaa.unam.mx GET / 1 identity close 
Starting connection.
Server response:
----------------------------------------
HTTP/1.1 200 OK
Date: Mon, 30 Oct 2023 06:33:30 GMT
Server: Apache/2.4.56 (Unix)
Last-Modified: Mon, 11 Jun 2007 18:53:14 GMT
ETag: "2d-432a5e4a73a80"
Accept-Ranges: bytes
Content-Length: 45
Connection: close
Content-Type: text/html

<html><body><h1>It works!</h1></body></html>

----------------------------------------
Connection to the server finished.

```

Ahora, una vez dentro del contenedor ejecuta:

```shell
./opt/tests.sh
```

**Nota:** El programa usa `python3`

## Evaluacion

### ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE?


### ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?

### ¿Para qué se usan los campos encoding y connection?

### Complicaciones

El unico error que tuve fue que al usar `python3` el socket
usa bytes como argumentos(HTTP_request), y al recibir datos,
estos tambien son bytes, y en `python2` estos son cadenas.

No fue un detalle que me quito mucho tiempo.
