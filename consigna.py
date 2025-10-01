"""
Entrega final - Playground Final project
En forma individual, crearás una aplicación web programada en Python con Django.
Esta web tendrá admin, perfiles, registro, páginas y formularios.

User story/brief:

- Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca del dueño de la página manejado en el route about/.

- Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Navbar, donde pueda moverme por las paginas)

Si no existe ninguna página mostrar un "No hay páginas aún". (opcional)

- Para editar o borrar pages debes estar logueado.

Piezas sugeridas

Te recomendamos incluir:

- NavBar

- Home

- About

- Login

- Signup

- Profile

- Logout

---------------------------
Get pages

Get page

Create page

Update Page
                            ------ CRUD
Delete page

Get profile

Update profile
-----------------------------

Requisitos base

Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto.

- Tener una app principal

- Entrega individual

- Subir a github

- Readme como la entrega 3

- Video de máximo 10 min que muestre la página y sus funcionalidades (con o sin audio)

--- programas que pueden utilizar freecam8, obs, filmora 12, etc.


No agregar la Base de datos (el archivo db.sqlite3) en la entrega. Debería estar en el .gitignore

Uso de herencia de templates. En el template base implementar la etiqueta nav de navegación que contenga los accesos que se crean necesarios para su página.

Exista gitignore con:

pycache

db.sqlite3

media
-------------------

Existencia del archivo requirements.txt actualizado.

Tener en cuenta al manejar forms con imágenes hay que adaptar el template, y la vista...no solo el modelo y el formulario.

Uso de mínimo 2 clases basadas en vista.

Uso de mínimo un mixin en una CBV y un decorador en una view común.

Una vista de inicio/home.

Acceso a una vista "Acerca de mí"/"About"

Crear un modelo principal (Blog/Post/Auto/Vendedor/Docente/etc) que contenga los siguiente campos como mínimo: 
- 2 Charfield, 
- 1 campo de imagen,
- 1 de fecha,
- 1 code,

 - Vista de listado de los objetos del modelo principal (modelo a elección). En la cual cada objeto mostrará solo algunos de sus datos.

- Mensaje que da aviso en caso de no haber ningún objeto creado o al utilizar el buscador no encontrar tampoco algún objeto.

Desde el listado:

poder acceder a una vista que muestre el detalle de el objeto seleccionado


poder acceder a una vista de creación, una de edición y una de borrado de objetos.


Registrar en el apartado de admin todos los modelos creados.

Tener una app (accounts/cuentas/etc) para el manejo de todas las vistas relacionadas al usuario/autenticación.

Desarrollar las vistas para un login, un logout y un registro para usuarios. En este último se debe solicitar: username, email, password.

Crear una vista de perfil donde se muestran los datos del usuario:


nombre


apellido


email


avatar


biografia/link/fecha de cumpleanios/etc.


Desde el perfil, crear un acceso a una vista de edición de estos datos. Agregar el cambio de password.

- Si el proyecyto es estilo Blog - Crear una app de Mensajeria.
- Si el proyecto es dif, crear una app personalizada.

EN TOTAL EL PROYECTO TIENE QUE TENER 3 APPS.

PUNTAZO A TENER EN CUENTA! PROBAR, PROBAR Y PROBAR ANTES DE

SUBIR EL CÓDIGO A GITHUB... ( no apurarse a hacer el commit y subir los

cambios porque puede generar algún problema sin darnos cuenta )

"""