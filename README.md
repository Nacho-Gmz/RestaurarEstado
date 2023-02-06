# Restaurar estado de ejecución
### Gómez Aldrete Luis Ignacio, Código: 216588253
Para esta práctica, se realizó una pequeña agenda en Python que permite almacenar el nombre y el número teléfonico de varios contactos, además cuenta con la funcionalidad de restaurar el estado de ejeución anterior gracias la uso de la librería *pickle*. 

El modulo *pickle* implementa protocolos binario que se encargan de la serialización y deserialización de las estructuras de objetos de Python. *Pickling* es el proceso por el cual una jerarquía de objetos de Python se convierte en un flujo de bytes, y *unpickling* es la operación inversa, mediante la cual un flujo de bytes (de un archivo binario o un objeto similar a bytes) se vuelve a convertir en una jerarquía de objetos.

La aplicación muestra un menú como el siguiente:

![image](https://user-images.githubusercontent.com/80866790/216936018-0e7bcf9a-815f-475f-a147-d20f1d92891d.png) 

![image](https://user-images.githubusercontent.com/80866790/216936792-13097feb-5895-453c-943c-89d9410fb70d.png)

Ya que el usuario haya agregado varios contactos, es posible salirse del programa y observar como es que hay un archivo nuevo generado por este llamado "*agenda.pickle*"

![image](https://user-images.githubusercontent.com/80866790/216936840-0c89199c-9613-4374-9f9e-57d3f2078d4d.png)

Este archivo es el que almacena todos los contactos que agregó el usuario y le permite recuperarlos cuando vuelva a entrar al programa si es que decide utilizar la opción de cargarlos.

![image](https://user-images.githubusercontent.com/80866790/216937255-62634cc7-b02d-4b0e-b61e-c9d51cd4e076.png)

Aquí se puede observar como al iniciar de nuevo el programa, no se cuenta con ningún contacto registrado, pero al elegir la opción de cargar los contactos, la librería *pickle* se encarga de recuperar los contactos que se habían almacenado en la ejecución anterior y los carga para tener acceso a ellos en la ejecución actual del programa.
