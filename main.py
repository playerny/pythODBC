import pyodbc
from datetime import date

today = date.today() #yyyy-mm-gg

def rename():
    print(connsrt)
    print(database)
    conn = pyodbc.connect(connsrt, autocommit=True)
    attualeDB = input("Inserire db da rinominare: ")
    newname = input("Inserire nuovo nome: ")
    query = "ALTER DATABASE "+ attualeDB +" MODIFY NAME = "+ newname +";"
    conn.execute(query)

def restore():
    print(connsrt)
    try:
        conn = pyodbc.connect(connsrt, autocommit=True)
        restoreDB = input("Inserire nome del database da ripristinare (es.: DB_NEW): ")
        pathDB = input("Inserire il percorso completo dov'è presente il file del database in formato .BAK (es.: C:/temp/DB.BAK): ")
        query = "RESTORE DATABASE "+ restoreDB +" FROM DISK = '"+ pathDB +"'"
        cursor = conn.cursor()
        cursor.execute(query)
        while cursor.nextset():
            pass
        cursor.close()
    except:
        print("Errore restore")

def drop():
    print(connsrt)
    conn = pyodbc.connect(connsrt, autocommit=True)
    delDB = input("Inserire nome del database da eliminare: ")
    dropDB = "DROP DATABASE "+ delDB +";"
    cursor = conn.cursor()
    cursor.execute(dropDB)
    while cursor.nextset():
        pass
        cursor.close()

# Inizio
cmd = '' # Opzione definita dall'utente. Inizialmente è vuota, così da poter gestire il loop while
server = input("Inserire istanza (es.: HOSTNAME\SQLEXPRESS): ")
port = input("Inserire porta di connessione (es.1433): ")
database = input("Inserire nome database (es.: master): ")
username = input("Inserire username: ")
password = input("Inserire password: ")
driver = '{ODBC Driver 17 for SQL Server}'
connsrt = 'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=' + port +';UID=' + username + ';PWD=' + password
while('test connessione' not in cmd or '1' not in cmd or 'test' not in cmd or 'rinomina' not in cmd or '2' not in cmd or 'restore' not in cmd or '3' not in cmd or 'elimina' not in cmd or '4' not in cmd or 'esci' not in cmd or '5' not in cmd):
    print("Seleziona una delle seguenti operazioni: ")
    print("1 - Test connessione")
    print("2 - Rinomina DB")
    print("3 - Restore DB")
    print("4 - Elimina DB")
    print("5 - Esci")
    cmd = input()
    cmd = cmd.lower()
    if('test' in cmd or '1' in cmd):
        try:
            conn = pyodbc.connect(connsrt)
            print("Connessione riuscita!")
            cmd = input("Continuare (y/n)? ")
            cmd = cmd.lower()
            if (cmd == 'y'):
                cmd = ''
            if (cmd == 'n'):
                exit()
        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print("Non è possibile connettersi. Verificare i seguenti errori:")
            print(sqlstate)
    if('rinomina' in cmd or '2' in cmd): # Rinomina DB
        try:
            rename() # Richiama la funzione rename()
        except:
            print("Si è verificato un errore.")
            exit()
    if('restore' in cmd or '3' in cmd):
        try:
            restore()
        except:
            print("Si è verificato un errore.")
            exit()
    if('elimina' in cmd or '4' in cmd):
        try:
            drop()
        except:
            print("Si è verificato un errore.")
            exit()
    if('esci' in cmd or '5' in cmd):
        exit()