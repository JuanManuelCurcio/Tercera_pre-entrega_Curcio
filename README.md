# BeLab - Plataforma para análisis de datos en ciencias del comportamiento

## Descripción:
BeLab está pensada como una plataforma comunitaria que brinde herramientas en línea para el análisis de datos en ciencias del comportamiento, psicología y áreas afines. El objetivo es que los usuarios puedan compartir sus dudas y proyectos, encontrar colaboradores, y recibir feedback o participación en sus estudios.

Para la entrega final, tengo pensado implementar al menos una funcionalidad relacionada con el análisis de datos, la cual estará accesible a través del botón **BeLab-Tools**.

Pido disculpas por la implementación rudimentaria del HTML; sin embargo, las funcionalidades solicitadas en la tarea funcionan según las pruebas realizadas.

## URL local de inicio: http://localhost:8000/app_belab/inicio/
(o si se abre el codigo del proyecto directamente y desde la consola del local host se corre el servidor tambien abre inicio)

## Explicación de la plataforma:

Se pueden probar las funcionalidades en cualquier orden. A continuación, explico cada botón de la interfaz:

### Botones (de derecha a izquierda):

- **Sign-in (formulario)**: Para registrar nuevos usuarios en la plataforma. La funcionalidad de inicio de sesión (log-in) aún no está implementada, pero el formulario para registrar usuarios nuevos ya funciona, aunque con un formato básico.
  - **Función:** Inserta un usuario nuevo en el modelo `Usuario`.

- **Log-in**: Esta funcionalidad no está implementada aún debido a que no hemos visto cómo manejar usuarios en el curso.

- **BeLab-Tools**: Aquí se implementarán las herramientas de análisis de datos descritas en la presentación del proyecto.

- **Consultas (formulario)**: Permite a los usuarios ingresar nuevas consultas. Estas consultas estarán relacionadas con el análisis de datos o diseños de investigación. Para la entrega final, se piensa implementar un sistema tipo blog donde las consultas sean visibles.
  - **Función:** Inserta una consulta en el modelo `Consulta`.

- **Proyectos**:
  - **Explorar proyectos**: Permite a los usuarios buscar proyectos cargados en la plataforma. La idea es que los usuarios puedan recibir feedback o encontrar colaboradores para sus proyectos.
    - **Función:** Busca proyectos ya guardados en la base de datos.
  
  - **Ingresar proyecto (formulario)**: Permite a los usuarios ingresar nuevos proyectos a la plataforma.
    - **Función:** Inserta un proyecto en el modelo `Proyectos`.

  - **Banner "Últimos proyectos" y pestañas**: Aún no está funcional. Aunque los proyectos están en la base de datos, para esta versión están hardcodeados. En el futuro, se implementará la funcionalidad para mostrar los últimos proyectos cargados o los más vistos.

- **Inicio**: Regresa a la página de inicio de la plataforma.

---

¡Muchas gracias por revisar la tarea! Quedo a la espera de cualquier comentario.
