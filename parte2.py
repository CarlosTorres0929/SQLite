import sqlite3

#conexion = sqlite3.connect('usuarios.db')
conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

#cursor.execute('''
#CREATE TABLE usuarios (
   # dni VARCHAR(9) PRIMARY KEY,
   # nombre VARCHAR(100),
  #  edad INTEGER,
 #   email VARCHAR(100)
#)
#''')

#usuarios = [
#    ('151454','Veronica',25,'muneka@gmail.com'),
 #   ('1446565','ibarguen',32,'carlosjara@gmail.com'),
  #  ('5645456','yuli',40,'yuli@gmail.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute("INSERT INTO usuarios VALUES ('546354646','juan',19,'juanejem@gmail.com')")


#cursor.execute('''
#CREATE TABLE productos (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
 #   nombre VARCHAR(100) NOT NULL,
  #  marca VARCHAR(50) NOT NULL,
   # precio FLOAT NOT NULL
#)
#''')

#productos = [
 #   ('teclado', 'logitech', 19.95),
  #  ('monitor 20', 'lg', 89.95),
#]
#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()
#for producto in productos:
 #   print(producto)

#cursor.execute('''
#CREATE TABLE usuarios (
 #   id INTEGER PRIMARY KEY AUTOINCREMENT,
  #  dni VARCHAR(9) UNIQUE,
   # nombre VARCHAR(100) NOT NULL,
    #edad INTEGER,
   # email VARCHAR(100)
#)
#''')

#usuarios = [
 #   ('151454','Veronica',25,'muneka@gmail.com'),
  #  ('1446565','ibarguen',32,'carlosjara@gmail.com'),
   # ('5645456','yuli',40,'yuli@gmail.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
#cursor.execute("INSERT INTO usuarios VALUES (null,'546354646','juan',19,'juanejem@gmail.com')")

conexion.commit()
conexion.close()
