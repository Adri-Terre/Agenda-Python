from peewee import *
import mysql.connector
from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter.messagebox import *
import module_variable as mod_var


def connection_db():

    """ este script permite conectarse con la tabla de la base de datos, y si no existe la crea con MySQL. """

    try:
        my_db = mysql.connector.connect(host="localhost", user="root", password="")
        mycursor = my_db.cursor()
        mycursor.execute("CREATE DATABASE AGENDA")

        print("Nueva base de datos AGENDA creada")

        my_db = mysql.connector.connect(
            host="localhost", user="root", password="", database="agenda"
        )
        mod_var.mycursor = my_db.cursor()
        mod_var.mycursor.execute(
            "CREATE TABLE contactos (ID INT AUTO_INCREMENT PRIMARY KEY, NOMBRE VARCHAR(255),APELLIDO VARCHAR(255),EMPRESA VARCHAR(255),EMAIL VARCHAR(255),TELEFONO VARCHAR(255),FOTO LONGBLOB)"
        )

        db_conectado = True
        return db_conectado

    except mysql.connector.Error as err:

        if err.errno == 2003:
            showinfo(
                "Conexión a base de datos",
                "No conectado. Verifique que los servicios de MySQL se estén ejecutando",
            )
            db_conectado = False
            return db_conectado

        else:

            mibase = MySQLDatabase(
                "agenda", user="root", password="", host="localhost", port=3306
            )

            class BaseModel(Model):
                class Meta:
                    database = mibase

            class Contactos(BaseModel):

                NOMBRE = CharField()
                APELLIDO = CharField()
                EMPRESA = CharField()
                EMAIL = CharField()
                TELEFONO = CharField()

            mibase.connect()
            mibase.create_tables([Contactos])
            db_conectado = True
            return db_conectado


def operacion_db(sql, val):

    """ esta funcion, a traves de Peewee, se utiliza para grabar/actualizar los contactos en la base de datos """

    my_db = MySQLDatabase(
        "agenda", user="root", password="", host="localhost", port=3306
    )
    mod_var.mycursor = my_db.cursor()
    mod_var.mycursor.execute(sql, val)
    my_db.commit()


def operacion_db_buscar(sql):

    """ esta funcion, a traves de Peewee, se utiliza para buscar los contactos en la base de datos """

    my_db = MySQLDatabase(
        "agenda", user="root", password="", host="localhost", port=3306
    )
    mod_var.mycursor = my_db.cursor()
    mod_var.mycursor.execute(sql)
    resultado = mod_var.mycursor.fetchall()

    return resultado
