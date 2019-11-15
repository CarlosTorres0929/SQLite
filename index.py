import sqlite3

conexion = sqlite3.connect('ejemplo.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit

# cursor.execute("INSERT INTO usuarios VALUES ('Carlos',21,'ct059489@gmail.com')")

#cursor.execute("SELECT * FROM usuarios")
#print(cursor)
#usuario = cursor.fetchone()
#print(usuario[2])

#usuarios = [
   # ('Veronica',25,'muneka@gmail.com'),
  #  ('ibarguen',32,'carlosjara@gmail.com'),
 #   ('yuli',40,'yuli@gmail.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

#cursor.execute("SELECT * FROM usuarios")

#usuarios = cursor.fetchall()

#for usuario in usuarios:
    #print("Nombre: ",usuario[0],"Email: ",usuario[2])



conexion.commit()
conexion.close()
