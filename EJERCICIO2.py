import pyodbc
import pandas as pd

# Lee el archivo Excel
df = pd.read_csv(r'C:\Users\hp\OneDrive\Documentos\DMD\country.csv') 

# Conexión a SQL Server con autenticación de Windows
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-7VMPCQ8\MSSQLSERVER_VEGA;'  # Nombre del servidor y la instancia
    'DATABASE=Country;'  # Nombre de la base de datos
    'Trusted_Connection=yes;'  # Autenticación de Windows
)
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CountryData' AND xtype='U')
    CREATE TABLE CountryData (
        Country VARCHAR(100),
        SafetySecurity FLOAT,
        PersonelFreedom FLOAT,
        Governance FLOAT,
        SocialCapital FLOAT,
        InvestmentEnvironment FLOAT,
        EnterpriseConditions FLOAT,
        MarketAccessInfrastructure FLOAT,
        EconomicQuality FLOAT,
        LivingConditions FLOAT,
        Health FLOAT,
        Education FLOAT,
        NaturalEnvironment FLOAT,


    )
''')
conn.commit()

# Inserta los datos en la tabla
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO CountryData (Country, SafetySecurity, PersonelFreedom, Governance, SocialCapital, InvestmentEnvironment, EnterpriseConditions, MarketAccessInfrastructure, EconomicQuality, LivingConditions, Health, Education, NaturalEnvironment)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', row['Country'], row['SafetySecurity'], row['PersonelFreedom'], row['Governance'], row['SocialCapital'], row['InvestmentEnvironment'], row['EnterpriseConditions'], row['MarketAccessInfrastructure'], row['EconomicQuality'], row['LivingConditions'], row['Health'], row['Education'], row['NaturalEnvironment'])

# Confirmar la inserción
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
