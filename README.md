# GradesCenter
#### Video Demo:  <URL HERE>
#### Description:

En mi proyecto final de CS50 he decidido realizar una aplicación web para manejar las calificaciones de los estudiantes de un colegio o una universidad. Mi propósito con esta propuesta será brindar una solución práctica, eficiente y amigable al momento en que una institución educativa (de la mano de sus profesores) requieran respaldar las notas de cada uno de sus estudiantes de forma segura y en un solo lugar; de igual manera, para que los alumnos tengan el acceso garantizado a las calificaciones de sus distintas materias. Todo esto inspirado en una situación problemática que sucede en mi universidad cada vez que llega la temporada de inscripciones e inicio de semestre: lamentablemente, el sistema se colapsa debido al volumen de usuarios activos y solicitudes a los servidores, ocasionando disgusto en la población estudiantil e inconvenientes relacionados a registrarse en las materias requeridas según el período en curso.

En mi aplicación web he empleando:
- Flask, para brindar dinamismo a mi utilidad
- SQL, para crear una base de datos desde cero, analizando todos los elementos necesarios para guardar la información de la forma más eficiente y ordenada posible
- Python, para que en alianza con Flask, pueda estructurar las rutas y el funcionamiento general de mi app, e incorporar validaciones del lado del servidor que vuelvan más robusto su entorno
- HTML, para estructurar cada una de las plantillas que he utilizado y brindar la información al usuario de una forma clara
- CSS, para decorar y embellecer la interfaz general de mi aplicación
- JavaScript, para hacer más interactiva la experiencia del usuario al momento de usar el software, a través de botones y diversas acciones


Archivos empleados en mi proyecto:
- "app.py": En primera instancia, se importan todas las librerías necesarias para el proyecto (os, requests, sqlite3, re, cs50, flask, werkzeug.security). Luego, se configura la aplicación mediante Flask y se vincula la base de datos. A continuación, son definidas las rutas (a través de funciones) que tendrá mi app, así como su lógica y comportamiento según los métodos HTTP: "GET" y "POST", esto derivado del proceder del usuario.
Son un total de 10 funciones:
1. after_request -

2. index - Consulta en la base de datos para filtrar la información y mostrar las materias que tiene a cargo un profesor. Es decir, las que está enseñando en un período determinado. Almacena el ID de la materia que seleccione el profesor para redirigirlo a la lista de estudiantes que están viendo esa materia en dicho periodo.

3. grades - Consulta en la base de datos para filtrar la información y mostrar el listado de alumnos que están inscritos en la materia seleccionada por el profesor. Almacena la nota ingresada por el profesor y actualiza su valor en la base de datos. Valida el ingreso de calificación entre un rango válido específico.

4. student - Consulta en la base de datos para filtrar la información y mostrar todo lo relacionado a las materias inscritas de un estudiante. 

5. add_subjects - Consulta en la base de datos las materias disponibles según la facultad en la que se encuentre el estudiante en cuestión, para así, desplegar un listado detallado y, según lo seleccionado, llevar a cabo la inscripción: insertando la información en la base de datos. Valida que el estudiante solo puede estar inscrito a una materia una única vez en un semestre.

6. login - Almacena la información proporcionada por el usuario para poder iniciar sesión y darle acceso al "home". Valida que dichos inputs sean ingresados correctamente. Consulta en la base de datos, según lo obtenido previamente, que el ID del usuario esté registrado y la contraseña sea correcta. Crea la sesión e identifica si ha sido un profesor o un estudiante.

7. logout - Cierra la sesión y olvida dicha información proporcionada por el usuario, para proteger mejor los datos de cada usuario.

8. subjects - Consulta en la base de datos las materias que tiene a su disposición un determinado profesor sin importar la facultad. Almacena el ID de la materia seleccionada para insertar los datos correspondientes a la base de datos y dejar registro de que dicho profesor está enseñando esa materia.

9. register - Almacena la información proporcionada por el usuario para poder registrarlo y añadir sus datos a la base de datos. Valida que los inputs solicitados sean ingresados de forma correcta, implementando la validación del lado del servidor. También valida que no pueden existir registrados con el mismo ID, el cual debe ser único por persona. Identifica si se ha registrado un profesor o un estudiante para que los datos sean conducidos a la tabla correcta en la base de datos.

10. edit_pass - Almacena la información proporcionada por el usuario para poder cambiar su contraseña. Valida dichos inputs corroborando que la contraseña ingresada sea la correcta y que la nueva sea confirmada dos veces; si todo está en orden, procede a actualizar el hash (almacenado en la base de datos) del usuario correspondiente.

11. settings - Solamente retorna una plantilla HTML para el usuario.

- "helpers.py":
- "gradescenter.db":
- "requirements.txt":
- "styles.css":
- "logo.ico":

Plantillas HTML:
- "layout":

- "index": Es la página principal cuando quien inicia sesión es un profesor. Muestra una tabla con la información de las materias que esta enseñando en ese período dicho maestro. En cada fila (que indica una materia) hay un botón que le permite al profesor ver el listado de estudiantes inscritos en dicha materia.

- "student": Es la página principal cuando quien inicia sesión es un estudiante. Muestra una tabla con la información de las materias inscritas de dicho estudiante, y le permite visualizar cual fueron sus notas al final del semestre.

- "add_subjects": Le permite al estudiante inscribirse en las materias que le correspondan según su período de estudio. Muestra una tabla con las materias identificadas por semestre y según la facultad a donde pertenezca. Cada fila tiene un boton para "inscribirse".

- "apology":

- "edit_pass":

- "grades": Muestra una tabla que es la lista de estudiantes inscritos en una determinada materia. Permite al profesor ver quien conforma su grupo de alumnos y también añadir o actualizar la nota de cada estudiante al final del semestre.

- "login":

- "register":

- "settings":

- "subjects":
