import sqlite3
conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()


#cursor.execute("SELECT * FROM usuarios WHERE id=1")
#cursor.execute("SELECT * FROM usuarios WHERE edad=27")
cursor.execute("UPDATE usuarios SET nombre='carlos torres', EDAD=30  WHERE dni='1145646545'")
#usuraio = cursor.fetchone()
usuraio = cursor.fetchall()
print(usuraio)

conexion.commit()
conexion.close()
