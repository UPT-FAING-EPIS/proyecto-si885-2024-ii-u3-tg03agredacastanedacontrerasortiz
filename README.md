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