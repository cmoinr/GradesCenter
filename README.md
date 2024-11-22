# GradesCenter
#### Video Demo:  <URL HERE>
#### Description:

In my final CS50 project I decided to create a web application to manage student grades at a university. My purpose with this proposal will be to provide a practical, efficient and user-friendly solution when an educational institution (with the help of its teachers) needs to back up the grades of each of its students safely and in one place; in the same way, so that students have guaranteed access to the grades of their different subjects.

All this was inspired by a problematic situation that occurs at my university every time the enrollment season and the beginning of the semester arrive: unfortunately, the system collapses due to the volume of active users and requests to the servers, causing displeasure in the student population and inconveniences related to registering for the required subjects according to the current period.

#### In my web application I have used:

- **Flask**, to provide dynamism to my utility

- **SQL**, to create a database from scratch, analyzing all the elements necessary to save the information in the most efficient and orderly way possible

- **Python**, so that in alliance with Flask, I can structure the routes and the general operation of my app, and incorporate server-side validations that make its environment more robust

- **HTML**, to structure each of the templates I have used and provide the information to the user in a clear way

- **CSS**, to decorate and beautify the general interface of my application

- **JavaScript**, to make the user's experience more interactive when using the software, through buttons and various actions

#### Files used in my project:

- <ins>**app.py:**</ins> First, all the libraries needed for the project are imported (os, requests, sqlite3, re, cs50, flask, werkzeug.security). Then, the application is configured using Flask and the database is linked. Next, the routes (through functions) that my app will have are defined, as well as its logic and behavior according to the HTTP methods: "GET" and "POST", this derived from the user's behavior.

_There are a total of 11 functions:_

1. **after_request** - It ensures that the browser where my app is run does not cache information, this to provide the user with dynamic content as required at the time. It also provides a layer of security by not allowing sensitive data to be cached.

2. **index** - Query the database to filter the information and show the subjects that a teacher is in charge of. That is, those that he is teaching in a given period. Stores the ID of the subject selected by the teacher to redirect her/him to the list of students who are viewing that subject in that period.

3. **grades** - Query in the database to filter the information and display the list of students who are enrolled in the subject selected by the teacher. Stores the grade entered by the teacher and updates its value in the database. Validates the grade entry within a specific valid range.

4. **student** - Query in the database to filter the information and display everything related to the subjects enrolled by a student.

5. **add_subjects** - Query in the database for the available subjects according to the faculty in which the student in question is enrolled, in order to display a detailed list and, depending on the selection, carry out the registration: inserting the information in the database. Validates that the student can only be enrolled in a subject once in a semester.

6. **login** - Stores the information provided by the user to be able to log in and give her/him access to the "home". Validates that the inputs are entered correctly. Checks the database, as previously obtained, that the user ID is registered and the password is correct. Creates the session and identifies whether it was a teacher or a student.

7. **logout** - Closes the session and forgets the information provided by the user, to better protect the data of each user.

8. **subjects** - Checks the database for the subjects available to a certain teacher regardless of the faculty. Stores the ID of the selected subject to insert the corresponding data into the database and record that said teacher is teaching that subject.

9. **register** - Stores the information provided by the user in order to register her/him and add her/his data to the database. Validates that the requested inputs are entered correctly, implementing server-side validation. It also validates that there cannot be registered users with the same ID, which must be unique per person. Identifies whether a teacher or a student has registered so that the data is taken to the correct table in the database.

10. **edit_pass** - Stores the information provided by the user in order to change his password. Validates these inputs by verifying that the password entered is correct and that the new password is confirmed twice; if everything is in order, proceeds to update the hash (stored in the database) of the corresponding user.

11. **settings** - Only returns an HTML template for the user.

- <ins>**helpers.py:**</ins> Two very important functions are implemented for the web application: 'apology', which provides the user with a personalized error message depending on the problem that has occurred; and 'login_required', which is responsible for providing security for access to certain routes in my application where access should only be possible after successfully logging in.

- <ins>**gradescenter.db:**</ins> This is one of the most important files in the project: it is the database, where all the information is going to be stored in a secure and structured way. I designed it from scratch, using paper and pencil, and was inspired by how I could handle all this data set (grades, names, surnames, professors) efficiently. 

_It consists of 7 SQL tables:_

1. **faculty** - Stores the name of the faculties and relates them to a unique ID.

2. **grades** - Stores the grade obtained by a student in a certain subject. This grade is related to the unique ID of the student and the subject.

3. **students** - Stores crucial data pertaining to the students: ID, names, surnames, current semester, credits obtained according to passing subjects, their login hash, ID of the faculty to which they belong.

4. **studying** - Stores the student ID related to the ID of the subject they are taking. It has a "many to many" relationship, since many students can see many subjects.

5. **subjects** - Stores crucial data about the subjects (the curriculum) taught at the school: unique ID, name, faculty where it is taught, semester it belongs to, and number of credit units awarded.

6. **teachers** - Stores crucial data pertaining to teachers: ID, first names, last names, and their login hash.

7. **teaching** - Stores the teacher's ID related to the subject ID they are teaching. It has a "many to many" relationship, since many teachers can teach many subjects.

- <ins>**requirements.txt:**</ins> Contains all the Python packages (libraries, modules) that are required for this project to work properly.

- <ins>**styles.css:**</ins> Contains all the CSS properties of the elements used through HTML. This is to give style and presentation to my web application.

- <ins>**logo.ico:**</ins> I designed this icon to further enhance the exterior finish of my interface.

#### HTML templates:

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
