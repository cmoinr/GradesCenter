# GradesCenter
#### Video Demo:  <URL HERE>
#### Description:

En mi proyecto final de CS50 he decidido realizar una aplicación web para manejar las calificaciones de los estudiantes en una universidad. Mi propósito con esta propuesta será brindar una solución práctica, eficiente y amigable al momento en que una institución educativa (de la mano de sus profesores) requieran respaldar las notas de cada uno de sus estudiantes de forma segura y en un solo lugar; de igual manera, para que los alumnos tengan el acceso garantizado a las calificaciones de sus distintas materias. 

Todo esto inspirado en una situación problemática que sucede en mi universidad cada vez que llega la temporada de inscripciones e inicio de semestre: lamentablemente, el sistema se colapsa debido al volumen de usuarios activos y solicitudes a los servidores, ocasionando disgusto en la población estudiantil e inconvenientes relacionados a registrarse en las materias requeridas según el período en curso.


En mi aplicación web he empleando:

    - Flask, para brindar dinamismo a mi utilidad

    - SQL, para crear una base de datos desde cero, analizando todos los elementos necesarios para guardar la información de la forma más eficiente y ordenada posible

    - Python, para que en alianza con Flask, pueda estructurar las rutas y el funcionamiento general de mi app, e incorporar validaciones del lado del servidor que vuelvan más robusto su entorno

    - HTML, para estructurar cada una de las plantillas que he utilizado y brindar la información al usuario de una forma clara

    - CSS, para decorar y embellecer la interfaz general de mi aplicación

    - JavaScript, para hacer más interactiva la experiencia del usuario al momento de usar el software, a través de botones y diversas acciones


Archivos empleados en mi proyecto:

- "app.py": En primera instancia, se importan todas las librerías necesarias para el proyecto (os, requests, sqlite3, re, cs50, flask, werkzeug.security). Luego, se configura la aplicación mediante Flask y se vincula la base de datos. A continuación, son definidas las rutas (a través de funciones) que tendrá mi app, así como su lógica y comportamiento según los métodos HTTP: "GET" y "POST", esto derivado del proceder del usuario.
Son un total de 11 funciones:
    1. after_request - Se encarga de que el navegador donde se ejecute mi app, no almacene información en caché, esto para brindar al usuario un contenido dinámico según se requiera en el momento. Además brinda una capa de seguridad al no permitir que quizá sea almacenen en caché datos sensibles.

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

- "helpers.py": Son implementadas 2 funciones de suma importancia para la aplicación web: 'apology', que brinda al usuario un mensaje de error personalizado según el inconveniente que haya sucedido; y 'login_required', que se encarga de brindar seguridad al acceso de determinadas rutas en mi aplicación donde sólo tras iniciar sesión correctamente se debiera poder acceder.

- "gradescenter.db": Este es uno de los archivos más importantes del proyecto: se trata de la base de datos, donde toda la información va a ser almacenada de forma segura y estructurada. Hice el diseño desde cero, a papel y lápiz, e inspirándome en cómo pudiera manejar todo este conjunto de datos (notas, nombres, apellidos, profesores) con eficiencia. Consta de 7 tablas SQL:
    1. faculty - Almacena el nombre de las facultades y las relaciona con un ID único.

    2. grades - Almacena la nota obtenida por un estudiante en una determinada materia. Esa calificación es relacionada con el ID único del estudiante y de la asignatura.

    3. students - Almacena los datos cruciales pertenecientes a los estudiantes: ID, nombres, apellidos, semestre actual, créditos obtenidos según aprobación de materias, su hash para iniciar sesión, ID de la facultad a la que pertenece.

    4. studying - Almacena el ID del estudiante relacionado con el ID de la materia que está cursando. Tiene una relación de "muchos a muchos", ya que muchos estudiantes pueden ver muchas asignaturas.

    5. subjects - Almacena los datos cruciales sobre las materias (el pensum) que se imparten en la casa de estudio: ID único, nombre, facultad donde se dicta, semestre al que pertenece, y número de unidades de créditos que otorga.

    6. teachers - Almacena los datos cruciales pertenecientes a los profesores: ID, nombres, apellidos, y su hash para iniciar sesión.

    7. teaching - Almacena el ID del profesor relacionado con el ID de la materia que está enseñando. Tiene una relación de "muchos a muchos", ya que muchos profesores pueden impartir muchas asignaturas.

- "requirements.txt": Contiene todos los paquetes de Python (bibliotecas, módulos) que son necesarios para que este proyecto funcione correctamente.

- "styles.css": Contiene todas las propiedades CSS de los elementos empleados a través de HTML. Esto para dar el estilo y la presentación a mi aplicación web.

- "logo.ico": Diseñé este icono para mejorar aún más el acabado exterior de mi interfaz.

Plantillas HTML:
- "layout": Es la plantilla (diseño) principal de la app. De este archivo se derivan las demás plantillas gracias a la implementación de Jinja. Despliega la barra de navegación principal y el pie de página.

- "index": Es la página principal cuando quien inicia sesión es un profesor. Muestra una tabla con la información de las materias que esta enseñando en ese período dicho maestro. En cada fila (que indica una materia) hay un botón que le permite al profesor ver el listado de estudiantes inscritos en dicha materia.

- "student": Es la página principal cuando quien inicia sesión es un estudiante. Muestra una tabla con la información de las materias inscritas de dicho estudiante, y le permite visualizar cual fueron sus notas al final del semestre.

- "add_subjects": Le permite al estudiante inscribirse en las materias que le correspondan según su período de estudio. Muestra una tabla con las materias identificadas por semestre y según la facultad a donde pertenezca. Cada fila tiene un boton para "inscribirse".

- "apology": Es una plantilla que muestra al usuario un mensaje de error personalizado. Facilita la comprensión del inconveniente ocurrido para mejorar la experiencia del usuario.

- "edit_pass": Muestra un pequeño formulario donde el usuario ingresará los datos necesarios para llevar a cabo el cambio de su contraseña satisfactoriamente.

- "grades": Muestra una tabla que es la lista de estudiantes inscritos en una determinada materia. Permite al profesor ver quien conforma su grupo de alumnos y también añadir o actualizar la nota de cada estudiante al final del semestre.

- "login": Es la página de inicio de sesión. Muestra el formulario adecuado para que el usuario ingrese sus datos y pueda ser redirigido a "index" o "student".

- "register": Muestra el formulario adecuado para que un usuario pueda registrarse al sistema. 

- "settings": Muestra algunos botones que le permitirán al usuario configurar algunos aspectos de su información almacenada.

- "subjects": Le permite al profesor añadir las materias que requiera según el período en curso. Muestra una tabla con las materias identificadas por semestre y según la facultad en que se enseña. Cada fila tiene un boton para "Seleccionar".
