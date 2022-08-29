# Trabajo-final
Trabajo final de programacion
Este trabajo consiste en una pagina de foros donde el usuario puede elegir el tema que prefiera dentro de las opciones que se encuentra dentro de la pagina y podra comentar lo que le parezca del tema que escogio.

Pasaremos con la parte funcional.

1. Primero debemos ejecutar el archivo "config.py" o Alt + f5.

![image](https://user-images.githubusercontent.com/107661618/187114747-b892b9ad-1f44-4294-b85c-b94aca5c4206.png)

2. Despues de ejecutar el archivo, debemos abrir el link del servidor dandole control + click.

![image](https://user-images.githubusercontent.com/107661618/187114962-cbe470ab-1bf3-4e3e-b4e1-758bcfac7144.png)

3. Ya despues de haber abierto el link del servidor, automaticamente se les abrira nuestra pagina web.

![image](https://user-images.githubusercontent.com/107661618/187115131-3015d170-3dcb-419b-83d1-7db9a85d100b.png)

4. Ya dentro de nuestra pagina, podra escoger una de las 4 opciones disponibles que tiene la pagina web, que son: deporte, comida, tecnologia y peliculas.

![image](https://user-images.githubusercontent.com/107661618/187115178-f26d6299-9bea-423b-b8c8-95b357ad086d.png)

5. Para entrar el comentario de uno de los 4 temas solo debe darle click al cuadro del tema que quiere.

![image](https://user-images.githubusercontent.com/107661618/187115490-47da2ad1-27ea-476d-8d23-929679e36dbc.png)

6. Ya despues de darle click al tema que quizo, se abrira otra pagina que podra ver la seccion que usted eligio y un cuadro donde podra poner el comentario que quiera.

![image](https://user-images.githubusercontent.com/107661618/187115894-be9f7e8f-3a88-45b7-add8-c7dc333c462b.png)

7. Cuando ingrese el comentario y el nombre, presionas a "enviar comentario", y quedara almacenado a una base de datos y se mostrara abajo del cuadro para ingresar datos.

![image](https://user-images.githubusercontent.com/107661618/187116110-8ad511a4-7ec2-425c-9808-092494a2fd23.png)


Ahora pasaremos a la parte practica.

1. Importamos las librerias necesarias.

![image](https://user-images.githubusercontent.com/107661618/187116206-947753cf-7368-481a-98d2-7d078474d9db.png)

2. Se creo una clase llamado "Aplicacion", donde tendran constructor con los siguientes parametros "self, nombre, duda, tabla" y conectamos la base de datos dentro del constructor y el respectivo manejador de la base de datos.

![image](https://user-images.githubusercontent.com/107661618/187116498-ff1bfb83-2e24-4b5f-bdaf-d475037b60ff.png)

3. Luego procedimos a crear una funcion dentro de la clase, con el parametro del constructor "self", para solicitar los siguientes datos "self.nombre, self.duda y self.tabla" y luego procedimos a insertar dichos valores en la base de datos y realizar los cambios.

![image](https://user-images.githubusercontent.com/107661618/187116801-ddab39df-97ee-42b9-9196-563c26cd1dea.png)

4. Despues procedimos a crear otra funcion, que es la que se encargara de extraer los datos de la base de datos y a retornar el nombre del archivo seleccionado en las rutas que se explicara mas adelante. Tambien retornamos en dicho archivo, los datos ya extraidos de las bases de datos.

![image](https://user-images.githubusercontent.com/107661618/187117254-6c3d44e6-4e74-4a3f-8408-42f21f50847b.png)

5. Luego se creo la variable es la que contiene el framework "Flask" con su respectivo nombre. Luego procedemos a crear una contraseña para el servidor.

![image](https://user-images.githubusercontent.com/107661618/187117470-080755dc-55d0-443f-8917-4d579a0e72a1.png)

6. Luego procedemos a crear las diferentes rutas para nuestro foro, dentro de ellas se encuentras las rutas de: comida, deporte, pelicula y tecnologia. Que nos sirven para retornar la plantilla de cada categoria.

![image](https://user-images.githubusercontent.com/107661618/187117695-85b0fe3c-ad44-485c-9e86-5cca4026922c.png)

7. Ahora procedemos a crear las rutas que nos permitiran extraer los datos desde nuestro formulario de html hasta nuestro servidor y asi poder tanto ingresar, como extraer dichos datos de la base de datos. El metodo que utilizamos en esta ruta es el metodo "POST", y procedemos en cada ruta a llamar la clase ya creada y a ingresarles, sus respectivos parametros. Una ves ingresados los parametros ejecutamos la funcion de insertar los datos y luego retornamos la funcion de extraer los datos.

![image](https://user-images.githubusercontent.com/107661618/187118106-f215811f-db0c-4491-908e-eb3aa41ec31b.png)
![image](https://user-images.githubusercontent.com/107661618/187118137-56a8085d-9f6f-472d-a1b6-5230d3c9353a.png)

8. Y al final, agregamos una condicional, que es la que nos permite inicializar el servidor.

![image](https://user-images.githubusercontent.com/107661618/187118306-0daf128f-bf07-4178-a6c4-32cdf0110271.png)
