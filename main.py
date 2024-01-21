
import pyodbc

server = '****.database.windows.net'
database = '****'
username = '***'
password = '****'

driver = '{ODBC Driver 17 for SQL Server}'

try:
    cnxn = pyodbc.connect('DRIVER=' + driver +
                      ';SERVER=' + server +
                      ';DATABASE=' + database +
                      ';UID=' + username +
                      ';PWD=' + password)

    cursor = cnxn.cursor()
    print('Connection established')

    # Create a table
    table_creation_query = '''
    CREATE TABLE Employees (
        Id INT PRIMARY KEY,
        Name NVARCHAR(50),
        Department NVARCHAR(50)
    )
    '''
    #cursor.execute(table_creation_query)
    #cnxn.commit()

    # Insert records into the table
    insert_query = '''
    INSERT INTO Employees (Id, Name, Department)
    VALUES
        (1, 'John Doe', 'IT'),
        (2, 'Jane Smith', 'Finance'),
        (3, 'Bob Johnson', 'HR')
    '''
    #cursor.execute(insert_query)
    #cnxn.commit()

    sql_query = f"SELECT * FROM Employees"

    # Выполнение запроса
    cursor.execute(sql_query)

    # Получение результатов
    data = cursor.fetchall()

    # Вывод данных
    print(f"Данные из таблицы Employees:")
    for row in data:
        print(row)

    # Close the cursor and connection
    cursor.close()
    cnxn.close()



except Exception as error:
    print('Cannot connect to SQL server', error)




