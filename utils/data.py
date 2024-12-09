import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "mssql+pymssql://adminsql:Upt2024!@bi-segunda-unidad.database.windows.net:1433/CICLO_UNIVERSITARIO"
)


with engine.connect() as connection:
    connection.execute(text("""
    IF NOT EXISTS (
        SELECT 1 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = 'Cursos'
    )
    BEGIN
        CREATE TABLE Cursos (
            CodigoCurso NVARCHAR(50) NOT NULL,
            NombreCurso NVARCHAR(255) NOT NULL,
            Matriculados INT NOT NULL,
            Aprobados INT NOT NULL,
            Desaprobados INT NOT NULL,
            Retiros INT NOT NULL,
            Abandonos INT NOT NULL,
            TotalLlevados INT NOT NULL,
            CantidadConvalidados INT NOT NULL,
            NotaMinima FLOAT NOT NULL,
            NotaMaxima FLOAT NOT NULL,
            Promedio FLOAT NOT NULL,
            DesviacionEstandar FLOAT NOT NULL,
            Semestre NVARCHAR(50) NOT NULL,
            PRIMARY KEY (CodigoCurso, Semestre)
        )
    END
    """))
    print("Tabla 'Cursos' creada o ya existía.")

excel_files = [
    './Consolidado/Consolidado_semestre_2020-I.xlsx',
    './Consolidado/Consolidado_semestre_2020-II.xlsx',
    './Consolidado/Consolidado_semestre_2021-I.xlsx',
    './Consolidado/Consolidado_semestre_2021-II.xlsx',
    './Consolidado/Consolidado_semestre_2022-I.xlsx',
    './Consolidado/Consolidado_semestre_2022-II.xlsx',
]

for file in excel_files:
    df = pd.read_excel(file, sheet_name='Hoja2')

    df['CodigoCurso'] = df['CODIGO CURSO'].astype(str)
    df['NombreCurso'] = df['ASIGNATURA'].astype(str)
    df['Matriculados'] = pd.to_numeric(df['MATRICULADOS'], downcast='integer')
    df['Aprobados'] = pd.to_numeric(df['APROBADOS'], downcast='integer')
    df['Desaprobados'] = pd.to_numeric(
        df['CANTIDAD DESAPROBADOS'], downcast='integer')
    df['Retiros'] = pd.to_numeric(df['CANTIDAD RETIRADOS'], downcast='integer')
    df['Abandonos'] = pd.to_numeric(
        df['CANTIDAD ABANDONADOS'], downcast='integer')
    df['TotalLlevados'] = pd.to_numeric(
        df['TOTAL LLEVADOS'], downcast='integer')
    df['CantidadConvalidados'] = pd.to_numeric(
        df['CANTIDAD CONVALIDADOS'], downcast='integer')
    df['NotaMinima'] = pd.to_numeric(
        df['NOTA MÍNIMA'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['NotaMaxima'] = pd.to_numeric(
        df['NOTA MÁXIMA'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['Promedio'] = pd.to_numeric(df['PROMEDIO'], errors='coerce').fillna(0.0)
    df['DesviacionEstandar'] = pd.to_numeric(
        df['DESVIACIÓN ESTÁNDAR'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['Semestre'] = file.split('_')[2].split('.')[0]

    with engine.connect() as connection:
        for index, row in df.iterrows():
            connection.execute(text("""
                INSERT INTO Cursos 
                (CodigoCurso, NombreCurso, Matriculados, Aprobados, Desaprobados, Retiros, Abandonos, TotalLlevados, 
                CantidadConvalidados, NotaMinima, NotaMaxima, Promedio, DesviacionEstandar, Semestre)
                VALUES (:CodigoCurso, :NombreCurso, :Matriculados, :Aprobados, :Desaprobados, :Retiros, 
                :Abandonos, :TotalLlevados, :CantidadConvalidados, :NotaMinima, :NotaMaxima, :Promedio, 
                :DesviacionEstandar, :Semestre)
            """), {
                'CodigoCurso': row['CodigoCurso'],
                'NombreCurso': row['NombreCurso'],
                'Matriculados': row['Matriculados'],
                'Aprobados': row['Aprobados'],
                'Desaprobados': row['Desaprobados'],
                'Retiros': row['Retiros'],
                'Abandonos': row['Abandonos'],
                'TotalLlevados': row['TotalLlevados'],
                'CantidadConvalidados': row['CantidadConvalidados'],
                'NotaMinima': row['NotaMinima'],
                'NotaMaxima': row['NotaMaxima'],
                'Promedio': row['Promedio'],
                'DesviacionEstandar': row['DesviacionEstandar'],
                'Semestre': row['Semestre']
            })
    print(f"Datos del archivo {file} insertados en la base de datos.")

print("Carga completada.")
