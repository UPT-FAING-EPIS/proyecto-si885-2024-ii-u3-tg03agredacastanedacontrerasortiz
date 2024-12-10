<center>

![logo-upt](../media/logo-upt.png)

# UNIVERSIDAD PRIVADA DE TACNA  
## FACULTAD DE INGENIERÍA  
### Escuela Profesional de Ingeniería de Sistemas

**Plataforma de análisis de datos de matriculados en la carrera de Ingeniería de Sistemas para la Universidad Privada de Tacna - PAMIS**

Curso: *Inteligencia de Negocios*  
Docente: *Mag. Patrick Cuadros Quiroga*

**Integrantes:**

<p style="font-size: 13px;">Agreda Ramirez, Jesus Eduardo  &emsp;&emsp;&emsp;&emsp;- &emsp;  (2021069823)
<br>Castañeda Centurion, Jorge Enrique &emsp; - &emsp; (2021069822)
<br>Contreras Lipa Alvaro Javier &emsp;&emsp;&emsp;&emsp;&emsp;&ensp; - &emsp;  (2021070020)
<br>Malaga Espinoza, Ivan Francisco &emsp;&emsp;&ensp; - &emsp; (2021071086)
<br>Ortiz Fernandez, Ximena Andrea &emsp;&emsp;&ensp; - &emsp;  (2021071080)</p>

**Tacna – Perú**  
***2024***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **Informe de Proyecto**

**Plataforma de análisis de datos de matriculados en la carrera de Ingeniería de Sistemas para la Universidad Privada de Tacna - PAMIS**

**Versión 3.0**

## **Control de Versiones**

| Versión | Hecha por | Revisada por | Aprobada por | Fecha      | Motivo           |
| :-----: | --------- | ------------ | ------------ | ---------- | ---------------- |
| 1.0     | JCC       | ACL          | JAR          | 27/08/2024 | Versión Original |
| 2.0     | XOF       | JAR          | IME          | 15/11/2024 | Versión Original |
| 3.0     | JAR       | XOF          | JCC          | 15/11/2024 | Versión Original |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## **Índice General**

## **Índice General**

1. [Antecedentes](#1)  

2. [Planteamiento del Problema](#2)  
   2.1 Problema  
   2.2 Justificación  
   2.3 Alcance  

3. [Objetivos](#3)  

4. [Marco Teórico](#4)  

5. [Desarrollo de la Solución](#5)  
   5.1 Análisis de Factibilidad  
   5.2 Tecnología de Desarrollo  
   5.3 Metodología de Implementación  

6. [Cronograma](#6)  

7. [Presupuesto](#7)  

8. [Conclusiones](#8)  

9. [Anexos](#9)  


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **Informe Final**

## 1. Antecedentes <a id="1"></a>

La Plataforma de Análisis de Matriculados en Ingeniería de Sistemas (PAMIS) nace como respuesta a la necesidad de mejorar la toma de decisiones académicas dentro de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna. En el entorno educativo actual, el acceso a datos detallados y personalizados es crucial para optimizar el rendimiento académico y la gestión institucional.

### Contexto:
*  En las instituciones educativas, el análisis de datos académicos ha adquirido una relevancia creciente, permitiendo identificar tendencias y patrones clave para la toma de decisiones estratégicas.
* PAMIS se alinea con esta necesidad al ofrecer una herramienta analítica que facilita el análisis de rendimiento académico, tasas de matriculación, índices de deserción y desempeño por curso.
* La plataforma está diseñada con tecnologías modernas como Power BI y servicios en la nube de Azure, garantizando una experiencia interactiva y accesible para estudiantes, docentes y administradores.

### Justificación Histórica:
* Se identificó la falta de herramientas específicas que permitan a los estudiantes visualizar su progreso académico y a la administración tomar decisiones basadas en datos. PAMIS busca llenar este vacío, apoyándose en metodologías modernas de análisis de datos​

## 2. Planteamiento del problema <a id="2"></a>

 ### Problema
En la actualidad, los estudiantes de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna (UPT) enfrentan diversos desafíos en la gestión de su rendimiento académico. Estos desafíos incluyen la falta de herramientas adecuadas para acceder a estadísticas detalladas sobre los cursos, la dificultad para tomar decisiones informadas basadas en datos claros y la ausencia de una plataforma centralizada para visualizar su progreso académico.

* Falta de acceso a información académica personalizada: La escuela dispone de un sistema administrativo que gestiona las estadísticas académicas a nivel institucional. Sin embargo, los estudiantes no tienen acceso directo a una plataforma que les permita visualizar de manera clara y personalizada datos como tasas de aprobación, índices de deserción y distribución de calificaciones en los cursos que les interesan. Esto limita su capacidad para evaluar y planificar su trayectoria académica de manera efectiva.
* Dificultades para tomar decisiones informadas: La carencia de herramientas accesibles y comprensibles para los estudiantes implica que deben tomar decisiones basadas en percepciones o información incompleta. Esta situación puede llevar a una planificación académica menos eficaz y a un rendimiento subóptimo en los cursos.
* Impacto en el rendimiento académico: Sin acceso a una visión detallada y precisa de su rendimiento académico, los estudiantes pueden enfrentar dificultades para identificar áreas de mejora y ajustar su enfoque de estudio, lo que afecta negativamente su desempeño y progreso académico.
* Necesidad de una plataforma de visualización de datos: Es fundamental desarrollar una herramienta analítica que permita a los estudiantes acceder a estadísticas relevantes y personalizadas sobre los cursos. Esta plataforma debería facilitar la toma de decisiones informadas, mejorar la planificación académica y optimizar el rendimiento académico de los estudiantes.

### Justificación
La implementación de PAMIS busca abordar estos problemas mediante:
* Acceso centralizado: Proporcionar a estudiantes y docentes una plataforma intuitiva que integre datos académicos clave.
* Visualización interactiva: Ofrecer gráficos y reportes detallados que faciliten la identificación de áreas críticas y la planificación académica.
* Toma de decisiones informadas: Apoyar a la administración en la optimización de recursos y estrategias académicas​

### Alcance
#### Inclusiones:
Desarrollo de una Aplicación en PowerBI:
* Creación de un dashboard interactivo en PowerBI que facilite la exploración visual de los datos académicos.
* Implementación de funcionalidades que permitan a los usuarios visualizar datos de matriculación, rendimiento académico y tasas de aprobación mediante gráficos dinámicos y tablas detalladas en PowerBI.

Funcionalidades Clave:
* Análisis detallado de los datos de matrículas, rendimiento académico y otros indicadores clave dentro del entorno de PowerBI.
* Exploración interactiva de los datos a través de visualizaciones en PowerBI para identificar patrones y tendencias que puedan guiar la toma de decisiones.

Soporte Tecnológico:
* Integración de capacidades avanzadas de análisis de datos y visualización en PowerBI para un rendimiento óptimo.
* Mantenimiento y actualizaciones continuas del dashboard en PowerBI, basadas en el feedback de los usuarios y las necesidades emergentes.
#### Exclusiones:
* Servicios Educativos Directos: PAMIS no proporcionará servicios educativos directos ni consultas académicas personalizadas.
* Gestión de Otros Programas Académicos: El enfoque estará limitado a la Ingeniería de Sistemas, y no se incluirá la gestión de otros programas académicos.
* Soporte Legal o Administrativo: La plataforma no ofrecerá asistencia legal ni soporte administrativo más allá del análisis de datos académicos.
* Soporte para Dispositivos Móviles: PAMIS no ofrecerá soporte ni optimización para dispositivos móviles, enfocándose únicamente en entornos de escritorio a través de PowerBI.

