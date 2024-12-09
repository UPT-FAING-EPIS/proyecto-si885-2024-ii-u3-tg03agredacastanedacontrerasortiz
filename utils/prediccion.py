import pyodbc
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sqlalchemy.sql import text

# Conexión usando pyodbc
connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:bi-segunda-unidad.database.windows.net,1433;"
    "Database=CICLO_UNIVERSITARIO;"
    "Uid=adminsql;"
    "Pwd=Upt2024!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# Crear motor de SQLAlchemy usando pyodbc
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")

try:
    with engine.begin() as connection:
        connection.exec_driver_sql("""
        IF NOT EXISTS (
            SELECT 1 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'predicciones'
        )
        BEGIN
            CREATE TABLE predicciones (
                Ciclo NVARCHAR(50) NOT NULL,
                Matriculados FLOAT NOT NULL,
                Aprobados FLOAT NOT NULL,
                Desaprobados FLOAT NOT NULL,
                PRIMARY KEY (Ciclo)
            )
        END
        """)
        print("Tabla 'predicciones' creada o ya existía.")

    # Verificar si la tabla fue creada correctamente
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'predicciones'")
        )
        if not result.fetchone():
            raise Exception("La tabla 'predicciones' no se creó correctamente.")
        else:
            print("La tabla 'predicciones' existe y está lista para usarse.")

except Exception as e:
    print(f"Error: {e}")

# Obtener datos para el modelo
query = """
SELECT Semestre, SUM(Matriculados) AS Matriculados, SUM(Aprobados) AS Aprobados, SUM(Desaprobados) AS Desaprobados
FROM Cursos 
GROUP BY Semestre 
ORDER BY Semestre
"""
data = pd.read_sql(query, engine)

# Procesar los datos
data['Semestre_Num'] = data['Semestre'].str.extract(r'(\d+)-').iloc[:, 0].astype(float) + \
    data['Semestre'].str.contains('II').astype(float) * 0.5

data = data.sort_values('Semestre_Num')

X = data[['Semestre_Num']]
y_matriculados = data['Matriculados']
y_aprobados = data['Aprobados']
y_desaprobados = data['Desaprobados']

# Crear y entrenar los modelos
X_train, X_test, y_train_matriculados, y_test_matriculados = train_test_split(
    X, y_matriculados, test_size=0.2, random_state=42)
model_matriculados = LinearRegression().fit(X_train, y_train_matriculados)

X_train, X_test, y_train_aprobados, y_test_aprobados = train_test_split(
    X, y_aprobados, test_size=0.2, random_state=42)
model_aprobados = LinearRegression().fit(X_train, y_train_aprobados)

X_train, X_test, y_train_desaprobados, y_test_desaprobados = train_test_split(
    X, y_desaprobados, test_size=0.2, random_state=42)
model_desaprobados = LinearRegression().fit(X_train, y_train_desaprobados)

# Predicciones para el próximo ciclo
next_cycle = np.array([[2023.5]])
predicted_matriculados = float(model_matriculados.predict(next_cycle)[0])
predicted_aprobados = float(model_aprobados.predict(next_cycle)[0])
predicted_desaprobados = float(model_desaprobados.predict(next_cycle)[0])

# Insertar predicciones en la tabla
with engine.connect() as connection:
    connection.execute(text("""
    INSERT INTO predicciones (Ciclo, Matriculados, Aprobados, Desaprobados)
    VALUES (:ciclo, :matriculados, :aprobados, :desaprobados)
    """), {
        'ciclo': '2023-II',
        'matriculados': predicted_matriculados,
        'aprobados': predicted_aprobados,
        'desaprobados': predicted_desaprobados
    })

print("Predicciones para el ciclo 2023-II:")
print(f"Matriculados: {predicted_matriculados:.2f}")
print(f"Aprobados: {predicted_aprobados:.2f}")
print(f"Desaprobados: {predicted_desaprobados:.2f}")
