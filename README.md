[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/OKCDjH9I)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17472715)




#  Plataforma de análisis de datos de matriculados en la carrera de ingeniería de sistemas para la universidad privada de Tacna - PAMIS

El propósito de PAMIS es proporcionar una plataforma tecnológica que permita a los estudiantes de la Escuela Profesional de Ingeniería de Sistemas abordar varios desafíos relacionados con el análisis del desempeño académico de sus compañeros. Estos desafíos incluyen la falta de acceso a herramientas analíticas detalladas, la necesidad de identificar patrones de rendimiento a lo largo del tiempo y la importancia de tomar decisiones estratégicas basadas en datos concretos.

## Integrantes
- **Agreda Ramirez, Jesus Eduardo			(2021069823)** 
- **Castañeda Centurion, Jorge Enrique		(2021069822)** 
- **Contreras Lipa, Alvaro Javier			(2021070020)** 
- **Málaga Espinoza, Ivan Francisco		(2021071086)**
- **Ortiz Fernandez, Ximena Andrea			(2021071080)**

## Curso
- Inteligencia de Negocios

## Docente
- Mag. Patrick Cuadros Quiroga

## Enlace a los datos
-  [Consolidado Semestre 2020 - I](https://docs.google.com/spreadsheets/d/1cIg5tDGIJB3h0LbpFJx4EUgkOMIlYVMK/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Consolidado Semestre 2020 - II](https://docs.google.com/spreadsheets/d/1eaYI-YMzZYpGdQ3vCbRQ28YCHEucd3Fi/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Consolidado Semestre 2021 - I](https://docs.google.com/spreadsheets/d/1oR_VQalTpQ3ZywmnBypG0NKYe4vTw7sf/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Consolidado Semestre 2021 - II](https://docs.google.com/spreadsheets/d/1x3-4pQaRQgEPI5ymfbOjxNAuNmJLEyI3/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Consolidado Semestre 2022 - I](https://docs.google.com/spreadsheets/d/1rwH7N_DOPicpMzaNN9rf5wD1CHzeQA0E/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Consolidado Semestre 2022 - II](https://docs.google.com/spreadsheets/d/10kJhI5DXXkWpJ0_mLp-LQxszpHnUWk9N/edit?usp=sharing&ouid=105683032286356296046&rtpof=true&sd=true)

-  [Link del reporte en PowerBI](https://app.powerbi.com/reportEmbed?reportId=0d97ad35-6197-41f4-8ff7-8956d59f99c0&autoAuth=true&ctid=b6b466ee-468d-4011-b9fc-fbdcf82ac90a)

## Diagramas Mermaid

- Diagrama de clase

```mermaid
classDiagram
    class Curso {
        +String codigoCurso
        +String nombreCurso
        +String semestre
        +int totalMatriculados
        +int totalAprobados
        +int totalDesaprobados
        +int totalRetiros
        +int totalAbandonos
        +int totalLlevados
        +int cantidadConvalidados
        +float notaMinima
        +float notaMaxima
        +float promedioNotas
        +float desviacionEstandarNotas
        +obtenerEstadisticas(): Map<String, Object>
        +calcularPromedioNotas(): float
        +calcularDesviacionEstandar(): float
        +actualizarEstadisticas(matriculados, aprobados, desaprobados, retiros): void
        +aplicarFiltroPorSemestre(semestre: String): List<Curso>
        +exportarReporte(formato: String): File
    }
```

- Diagrama Contenedor
```mermaid
graph TD
    subgraph Aplicación_Web
        A_Interfaz[Interfaz de Usuario]
    end

    subgraph Servidor_Backends
        B1[Gestiona la lógica de negocio]
        B2[Procesa las solicitudes del frontend]
    end

    subgraph Terraform
        C1[Automatiza la configuración de infraestructura en Azure]
    end

    subgraph Azure
        E[Base de datos]
    end

    A_Interfaz -->|Solicita datos| B1
    B1 -->|Consulta/Actualiza datos académicos| E
    B2 -->|Procesa solicitudes| A_Interfaz
    B1 -->|Gestiona y provisiona| C1
    C1 -->|Configura infraestructura| E

```

- Diagrama Contextual
```mermaid
graph LR
    A[Administrador / Docente] -->|Interactúa con los gráficos y análisis académicos| PAMIS
    PAMIS -->|Provee datos académicos| B[Base de Datos]
    PAMIS -->|Gestiona la infraestructura y recursos en Azure| C[Terraform]

```

- Diagrama de Actividades CU-01 “Consultar estadísticas académicas”
```mermaid
sequenceDiagram
    participant Estudiante as Estudiante (Actor)
    participant Sistema as Sistema (PAMIS)

    Estudiante->>Sistema: Acceder a la plataforma PAMIS desde su navegador
    Sistema-->>Estudiante: Muestra la pantalla principal con las secciones disponibles (Análisis de Matrículas, Desempeño Académico, etc.)
    Estudiante->>Sistema: Selecciona una sección (por ejemplo, "Análisis de Matrículas")
    Sistema-->>Estudiante: Carga y muestra los gráficos relacionados con las estadísticas de matrículas
    Estudiante->>Sistema: Navega por los gráficos y observa los datos mostrados
    Sistema-->>Estudiante: Permite la interacción con los gráficos (detalles al pasar el cursor o hacer clic)

```

-Diagrama de Actividades CU-02 “Aplicar filtros a los gráficos”
```mermaid
sequenceDiagram
    participant Estudiante as Estudiante (Actor)
    participant Sistema as Sistema (PAMIS)

    Estudiante->>Sistema: Selecciona un gráfico dentro de una sección de análisis
    Sistema-->>Estudiante: Muestra el gráfico con datos generales y las opciones de filtros disponibles

    Estudiante->>Sistema: Elige un filtro (e.g., "Semestre: 2021-I")
    Sistema-->>Sistema: Actualiza el gráfico para reflejar los datos correspondientes al filtro seleccionado
    Sistema-->>Estudiante: Muestra el gráfico actualizado

    Estudiante->>Sistema: Elige un segundo filtro (e.g., "Curso: Auditoría de Sistemas")
    Sistema-->>Sistema: Combina los filtros aplicados y actualiza el gráfico de manera interactiva
    Sistema-->>Estudiante: Muestra el gráfico interactivo actualizado

```
-Diagrama de Actividades CU-03 “Exportar reportes”
```mermaid
sequenceDiagram
    participant Estudiante as Estudiante (Actor)
    participant Sistema as Sistema (PAMIS)

    Estudiante->>Sistema: Selecciona un gráfico dentro de una sección
    Sistema-->>Estudiante: Muestra el gráfico con la opción "Exportar datos"

    Estudiante->>Sistema: Hace clic en la opción "Exportar datos"
    Sistema-->>Estudiante: Muestra un cuadro de diálogo con las opciones de exportación ("Datos resumidos" o "Datos con diseño actual")

    Estudiante->>Sistema: Selecciona "Datos resumidos"
    Estudiante->>Sistema: Elige un formato (por ejemplo, "XLSX")
    Sistema-->>Sistema: Habilita los formatos disponibles para exportar (XLSX y CSV)

    Estudiante->>Sistema: Hace clic en el botón de descarga
    Sistema-->>Estudiante: Procesa la exportación y genera el archivo en el formato seleccionado
    Sistema-->>Estudiante: Descarga el archivo al dispositivo del estudiante

```

-Diagrama de actividades Inicial
```mermaid
sequenceDiagram
    participant Estudiante as Estudiante (Usuario)
    participant Sistema as Sistema (PAMIS)

    Estudiante->>Sistema: Accede a la plataforma PAMIS desde su navegador
    Sistema-->>Estudiante: Muestra la pantalla principal con las secciones de análisis

    Estudiante->>Sistema: Selecciona una sección (por ejemplo, "Análisis de Matrículas")
    Sistema-->>Estudiante: Carga y muestra los gráficos interactivos relacionados

    Estudiante->>Sistema: Navega por los gráficos y observa los datos
    Estudiante->>Sistema: Selecciona un gráfico para aplicar filtros
    Sistema-->>Estudiante: Muestra las opciones de filtros disponibles

    Estudiante->>Sistema: Aplica un filtro (por ejemplo, "Semestre: 2021-I")
    Sistema-->>Estudiante: Actualiza el gráfico según los filtros seleccionados
    Sistema-->>Estudiante: Muestra el gráfico actualizado con los datos filtrados

    Estudiante->>Sistema: Selecciona la opción de exportar datos del gráfico
    Estudiante->>Sistema: Selecciona el formato de exportación (por ejemplo, "XLSX")
    Sistema-->>Sistema: Procesa la exportación y genera el archivo
    Sistema-->>Estudiante: Descarga el archivo al dispositivo del estudiante

```

-Diagrama de componentes
```mermaid
graph TD
    Database["Base de Datos (CICLO_UNIVERSITARIO)"] --> PowerBI["Power BI"]
    PowerBI --> Model["Modelo de Datos"]
    Model --> Transformations["Transformaciones DAX"]
    Transformations --> Metrics["Páginas de Presentación"]
    Metrics -->|Proveen datos base| Tables["Gráficos y Tablas «UI»"]
    Metrics --> Comparative["Análisis Comparativo"]
    Metrics --> Approval["Índice de Desaprobación"]
    Metrics --> Performance["Desempeño Académico"]
    Metrics --> Enrollment["Análisis Matrícula"]
    Users["Usuarios"] -->|Interacción| Tables

```

-Diagrama de Paquetes
```mermaid
graph TD
    subgraph PAMIS
        AzureDB["Base de Datos Azure"] --> PowerBIService["Power BI Service"]
        Dashboards --> PowerBIService
    end
    PublicationServices["Servicios de publicación Power BI"] --> PowerBIService

```

-Diagrama de Proceso Propuesto
```mermaid
sequenceDiagram
    participant Estudiante as Estudiante (Usuario)
    participant Sistema as Sistema (PAMIS)

    Estudiante->>Sistema: Accede a la plataforma PAMIS desde su navegador
    Sistema-->>Estudiante: Muestra la pantalla principal con las secciones de análisis

    Estudiante->>Sistema: Selecciona una sección (por ejemplo, "Análisis de Matrículas")
    Sistema-->>Estudiante: Carga y muestra los gráficos interactivos relacionados

    Estudiante->>Sistema: Navega por los gráficos y observa los datos
    Estudiante->>Sistema: Selecciona un gráfico para aplicar filtros
    Sistema-->>Estudiante: Muestra las opciones de filtros disponibles

    Estudiante->>Sistema: Aplica un filtro (por ejemplo, "Semestre: 2021-I")
    Sistema-->>Estudiante: Actualiza el gráfico según los filtros seleccionados
    Sistema-->>Estudiante: Muestra el gráfico actualizado con los datos filtrados

    Estudiante->>Sistema: Aplica un segundo filtro (por ejemplo, "Curso: Auditoría de Sistemas")
    Sistema-->>Estudiante: Actualiza el gráfico según los filtros seleccionados
    Sistema-->>Estudiante: Muestra el gráfico actualizado con los datos filtrados

    Estudiante->>Sistema: Selecciona la opción de exportar datos del gráfico
    Estudiante->>Sistema: Selecciona el formato de exportación (por ejemplo, "XLSX")
    Sistema-->>Estudiante: Procesa la exportación y genera el archivo
    Sistema-->>Estudiante: Descarga el archivo al dispositivo del estudiante

```
-Diagrama de Secuencia de CU01 “Consultar estadísticas académicas”
```mermaid
sequenceDiagram
    actor Estudiante as Estudiante
    participant Dashboard as Dashboard Principal «Interfaz»
    participant AnalisisMatriculas as Sección de Análisis de Matrículas «Frontera»
    participant ControlGraficos as Control de Gráficos «Control»

    Estudiante->>Dashboard: Accede a la plataforma PAMIS
    Dashboard-->>Estudiante: Muestra las secciones disponibles (Análisis de Matrículas, Desempeño Académico, etc.)

    Estudiante->>Dashboard: Selecciona "Análisis de Matrículas"
    Dashboard->>AnalisisMatriculas: Cargar gráficos de estadísticas de matrículas
    AnalisisMatriculas-->>Dashboard: Envía gráficos cargados

    Dashboard-->>Estudiante: Muestra gráficos interactivos
    Estudiante->>Dashboard: Navega por los gráficos (interacción)
    Dashboard->>ControlGraficos: Actualiza detalles en los gráficos según la interacción
    ControlGraficos-->>Dashboard: Envía detalles actualizados

    Dashboard-->>Estudiante: Muestra los detalles específicos

```

-Diagrama de Secuencia de CU02 “Aplicar filtros a los gráficos”
```mermaid
sequenceDiagram
    actor Estudiante as Estudiante
    participant GraficoInteractivo as Gráfico Interactivo «Frontera»
    participant ControlFiltros as Control de Filtros «Control»
    participant ControlGraficos as Control de Gráficos «Control»
    participant DatosEstadisticos as Datos Estadísticos «Entidad»

    Estudiante->>GraficoInteractivo: Selecciona un gráfico dentro de una sección
    GraficoInteractivo-->>Estudiante: Muestra gráfico con datos generales y opciones de filtros disponibles

    Estudiante->>GraficoInteractivo: Elige un filtro (e.g., Semestre: 2021-I)
    GraficoInteractivo->>ControlFiltros: Solicita datos filtrados por semestre
    ControlFiltros->>DatosEstadisticos: Solicita datos correspondientes al filtro
    DatosEstadisticos-->>ControlFiltros: Devuelve datos correspondientes al filtro
    ControlFiltros-->>GraficoInteractivo: Actualiza gráfico con datos filtrados
    GraficoInteractivo-->>Estudiante: Actualiza gráfico mostrado

    Estudiante->>GraficoInteractivo: Selecciona un segundo filtro (e.g., Curso: Auditoría de Sistemas)
    GraficoInteractivo->>ControlFiltros: Solicita datos combinados (Semestre + Curso)
    ControlFiltros->>DatosEstadisticos: Solicita datos combinados
    DatosEstadisticos-->>ControlFiltros: Devuelve datos combinados
    ControlFiltros-->>GraficoInteractivo: Actualiza gráfico con datos combinados
    GraficoInteractivo-->>Estudiante: Actualiza gráfico interactivo mostrado

```
-Diagrama de Secuencia de CU03 “Exportar reportes”
```mermaid
sequenceDiagram
    actor Estudiante as Estudiante
    participant GraficoInteractivo as Gráfico Interactivo «Frontera»
    participant ControlFiltros as Control de Filtros «Control»
    participant ControlGraficos as Control de Gráficos «Control»
    participant DatosEstadisticos as Datos Estadísticos «Entidad»

    Estudiante->>GraficoInteractivo: Selecciona un gráfico dentro de una sección
    GraficoInteractivo-->>Estudiante: Muestra gráfico con datos generales y opciones de filtros disponibles

    Estudiante->>GraficoInteractivo: Elige un filtro (e.g., Semestre: 2021-I)
    GraficoInteractivo->>ControlFiltros: Solicita datos filtrados por semestre
    ControlFiltros->>DatosEstadisticos: Devuelve datos correspondientes al filtro
    DatosEstadisticos-->>ControlFiltros: Devuelve datos correspondientes al filtro
    ControlFiltros-->>GraficoInteractivo: Actualiza gráfico con datos filtrados
    GraficoInteractivo-->>Estudiante: Actualiza gráfico mostrado

    Estudiante->>GraficoInteractivo: Selecciona un segundo filtro (e.g., Curso: Auditoría de Sistemas)
    GraficoInteractivo->>ControlFiltros: Solicita datos combinados (Semestre + Curso)
    ControlFiltros->>DatosEstadisticos: Solicita datos combinados
    DatosEstadisticos-->>ControlFiltros: Devuelve datos combinados
    ControlFiltros-->>GraficoInteractivo: Actualiza gráfico con datos combinados
    GraficoInteractivo-->>Estudiante: Actualiza gráfico interactivo mostrado

```

-Diagrama ER
```mermaid
erDiagram
    Cursos {
        VARCHAR NombreCurso
        INT Matriculados
        INT Aprobados
        INT Desaprobados
        INT Retiros
        INT Abandonos
        INT TotalLlevados
        INT CantidadConvalidados
        FLOAT NotaMinima
        FLOAT NotaMaxima
        FLOAT Promedio
        FLOAT DesviacionEstandar
        NVARCHAR(50) CodigoCurso
        NVARCHAR(50) Semestre
    }

```
-Organigrama
```mermaid
graph TD
    A[Consejo de Facultad] --> B[Decanato]
    B --> C[Comisión de Planificación]
    B --> D[Comisión Académico Curricular y de Evaluación Docente]
    B --> E[Comisión de Aseguramiento de la Calidad]
    B --> F[Secretaría Académica Administrativa]
    
    F --> G[Escuela Profesional de Ingeniería Electrónica]
    F --> H[Escuela Profesional de Ingeniería de Sistemas]
    F --> I[Escuela Profesional de Ingeniería Civil]
    F --> J[Escuela Profesional de Ingeniería Agroindustrial]
    F --> K[Escuela Profesional de Ingeniería Ambiental]
    F --> L[Escuela Profesional de Ingeniería Industrial]
    F --> M[Unidad de Postgrado y/o Segunda Especialidad]
    F --> N[Unidad de Investigación]
    F --> O[Unidad de Responsabilidad Social Universitaria]
    F --> P[Centro de Producción de Bienes y Prestación de Servicios]

```