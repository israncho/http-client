# http-client
Implementacion de un pequeño cliente HTTP con python para la practica 4
de la materia de redes de computadoras 2024-1.

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

- **HEAD:** Este metodo hace lo mismo que **GET** pero sin recuperar
    el cuerpo de la respuesta. Principalmente para recuperar metadatos,
    nos puede apoyar para verificar si un servicion esta disponible.

- **GET:** Es el metodo para solicitar un recurso especificado del servidor.
    Este metodo solo se debe usar para obtener datos.

- **POST:** Envia a un servidor datos para interactuar con este y muy
    posiblemente cambiar el estado del mismo.

- **PUT:** Se utiliza para crear o actualiza recursos en un servidor.

- **DELETE:** Se utiliza para solicitar que un recurso en un servidor sea
    borrado. El uso de este debe ser con precaucion pues muchas veces
    no se quiere que un usuario tenga la capacidad de realizar esto.

### ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?

- **100-199:** Respuestas informativas.

- **200-299:** Respuestas de exito.

- **300-399:** Respuestas de redireccion.

- **400-499:** Errores por parte del cliente.

- **500-599:** Errores por parte del servidor.

### ¿Para qué se usan los campos encoding y connection?

- **enconding:** Este campo se utiliza para especificar los tipos
    de codificacion que entiende el cliente, posteriormente el servidor
    elige uno de estos tipos para codificar las respuestas.

- **connection:** Este campo es para especificar como se va a manejar la
    conexion entre el cliente y el servidor despues de que la transaccion
    se complete.

#### Referencias consultadas:

- [https://en.wikipedia.org/wiki/HTTP#Request_methods](https://en.wikipedia.org/wiki/HTTP#Request_methods)

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding)

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection)


### Complicaciones

El unico error que tuve fue que al usar `python3` el socket
usa bytes como argumentos(HTTP_request), y al recibir datos,
estos tambien son bytes, y en `python2` estos son cadenas.

No fue un detalle que me quito mucho tiempo.
