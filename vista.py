from tkinter import *
from tkinter.messagebox import *
import sys
from module_base_de_datos import connection_db
import modulo
import controller


def limpiar():
    """ esta funcion, a traves del controller, limpia los campos de la pantalla"""
    controller.control_limpiar()


def buscartodos():

    """ esta funcion, a traves del controller, busca todos los contactos"""
    datos_hacia_controller = "todos"
    controller.control_buscartodos(datos_hacia_controller)


def buscar_contacto():

    """ esta funcion, a traves del controller, busca un contacto específico"""
    controller.control_buscarcontacto()


def editar():

    """ esta funcion, a traves del controller, llama y ejecuta todo lo relacionado con el menú editar, dentro del cual se puede buscar, editar o eliminar un contacto en la base de datos"""

    global contacto_buscar
    global datos_nombre
    global datos_apellido
    global datos_email
    global datos_empresa
    global datos_movil
    global codigo
    global win_modificar
    global w9
    import module_variable as mod_var

    mod_var.ventana_open_editar = True
    mod_var.ventana_open = False

    mod_var.func_modificar = True
    mod_var.var1 = BooleanVar()
    mod_var.var2 = BooleanVar()

    win_modificar = Toplevel()
    win_modificar.title("Editar contacto")
    win_modificar.geometry("530x390")

    """ labels del cuadro del menú editar """

    w1 = Label(win_modificar, text="NOMBRE")
    w1.place(x=20, y=60)
    w2 = Label(win_modificar, text="APELLIDO")
    w2.place(x=20, y=100)
    w3 = Label(win_modificar, text="EMPRESA")
    w3.place(x=20, y=140)
    w4 = Label(win_modificar, text="E-MAIL")
    w4.place(x=20, y=180)
    w5 = Label(win_modificar, text="TELÉFONO")
    w5.place(x=20, y=220)
    w6 = Label(win_modificar, text="CONTACTO")
    w6.place(x=20, y=20)

    """ inputs del cuadro del menú editar """

    contacto_buscar = Entry(win_modificar)
    contacto_buscar.configure(width=30)
    contacto_buscar.place(x=150, y=20)
    contacto_buscar.focus_set()

    datos_nombre = Entry(win_modificar)
    datos_nombre.configure(width=30)
    datos_nombre.place(x=150, y=60)
    datos_nombre.focus_set()

    datos_apellido = Entry(win_modificar)
    datos_apellido.configure(width=30)
    datos_apellido.place(x=150, y=100)
    datos_apellido.focus_set()

    datos_empresa = Entry(win_modificar)
    datos_empresa.configure(width=30)
    datos_empresa.place(x=150, y=140)
    datos_empresa.focus_set()

    datos_email = Entry(win_modificar)
    datos_email.configure(width=30)
    datos_email.place(x=150, y=180)
    datos_email.focus_set()

    datos_movil = Entry(win_modificar)
    datos_movil.configure(width=30)
    datos_movil.place(x=150, y=220)
    datos_movil.focus_set()

    Button(
        win_modificar,
        text="Buscar",
        width=20,
        command=controller.control_buscar_editar,
        anchor=CENTER,
    ).place(x=350, y=14)

    Button(
        win_modificar,
        text="Actualizar contacto",
        width=20,
        command=controller.control_pasaje_regex,
        anchor=CENTER,
    ).place(x=350, y=100)

    Button(
        win_modificar,
        text="Eliminar contacto",
        width=20,
        command=controller.control_pasaje_eliminar,
        anchor=CENTER,
    ).place(x=350, y=250)

    Button(
        win_modificar,
        text="Limpiar_pantalla",
        width=20,
        command=controller.control_clear_window,
        anchor=CENTER,
    ).place(x=350, y=310)

    Checkbutton(
        win_modificar, text="Actualizar foto perfil", variable=mod_var.var2
    ).place(x=200, y=250)

    w9 = Label(win_modificar, text="> FOTO DE PERFIL <")
    w9.place(x=10, y=310)


def alta():

    """ esta funcion, a traves del controller, realiza el alta con la base de datos """

    import module_variable as mod_var

    global codigo
    global datos_nombre
    global datos_apellido
    global datos_empresa
    global datos_email
    global datos_movil
    global win_alta
    global image_64_encode

    mod_var.ventana_open = True
    mod_var.ventana_open_editar = False
    mod_var.func_modificar = False

    mod_var.image_64_encode = ""
    mod_var.var1 = BooleanVar()
    mod_var.var2 = BooleanVar()

    win_alta = Toplevel()
    win_alta.title("Alta de contacto")
    win_alta.geometry("400x300")

    """ labels del cuadro del menú alta """

    w1 = Label(win_alta, text="NOMBRE")
    w1.place(x=20, y=20)
    w2 = Label(win_alta, text="APELLIDO")
    w2.place(x=20, y=60)
    w3 = Label(win_alta, text="EMPRESA")
    w3.place(x=20, y=100)
    w4 = Label(win_alta, text="E-MAIL")
    w4.place(x=20, y=140)
    w5 = Label(win_alta, text="TELÉFONO")
    w5.place(x=20, y=180)

    """ inputs del cuadro del menú alta """

    datos_nombre = Entry(win_alta)
    datos_nombre.configure(width=30)
    datos_nombre.place(x=170, y=20)
    datos_nombre.focus_set()

    datos_apellido = Entry(win_alta)
    datos_apellido.configure(width=30)
    datos_apellido.place(x=170, y=60)
    datos_apellido.focus_set()

    datos_empresa = Entry(win_alta)
    datos_empresa.configure(width=30)
    datos_empresa.place(x=170, y=100)
    datos_empresa.focus_set()

    datos_email = Entry(win_alta)
    datos_email.configure(width=30)
    datos_email.place(x=170, y=140)
    datos_email.focus_set()

    datos_movil = Entry(win_alta)
    datos_movil.configure(width=30)
    datos_movil.place(x=170, y=180)
    datos_movil.focus_set()

    Checkbutton(win_alta, text="Añadir foto perfil", variable=mod_var.var1).place(
        x=25, y=230
    )
    Button(
        win_alta,
        text="Alta de contacto",
        width=20,
        command=controller.control_pasaje_regex,
        anchor=CENTER,
    ).place(x=225, y=230)


def call_exportar():

    """ esta funcion, a traves del controller, exporta los datos de la agenda en .pdf, .csv, xml, json """

    controller.control_exportar()


def integrantes():

    """ esta funcion crea una pantalla donde se muestran los integrantes del proyecto"""

    win = Toplevel()
    win.title("Integrantes")
    win.geometry("300x100")
    label_integrantes = Label(win, text="TERRENI ADRIAN\n\n" "LAUTARO MAZZOLDI\n",)

    label_integrantes.place(x=100, y=20)


def curso():

    """ esta funcion crea una pantalla en donde se muestran los datos del curso """

    win2 = Toplevel()
    win2.title("Curso")
    win2.geometry("350x100")
    label_curso = Label(
        win2,
        text="UNIVERSIDAD TECNOLÓGICA NACIONAL\n"
        "DIPLOMATURA PYTHON - NIVEL AVANZADO\n",
    )

    label_curso.place(x=50, y=30)


# ----------------------------SECCIÓN GRÁFICA DE LA AGENDA------------------------

master = Tk()

e1_input = Entry(master)
e1_input.configure(width=30)
e1_input.place(x=170, y=14)
e1_input.focus_set()

""" cuadro de texto donde van a aparecer los datos de contacto """

datos_contacto = Text(master)
datos_contacto.place(x=380, y=40, width=200, height=200)

""" Aquí se crea la pantalla principal """

master.geometry("620x300")
master.title("Agenda")
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
# --------Archivo--------------------------
menu.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Exportar", command=call_exportar)
filemenu.add_separator()
filemenu.add_command(label="Cerrar", command=master.quit)
# ---------Menu----------------------------
Menu_x = Menu(menu)
menu.add_cascade(label="Menu", menu=Menu_x)
Menu_x.add_command(label="Alta", command=alta)
Menu_x.add_separator()
Menu_x.add_command(label="Editar", command=editar)
# ---------Acerca de-----------------------
acerca_de = Menu(menu)
menu.add_cascade(label="Acerca de", menu=acerca_de)
acerca_de.add_command(label="Integrantes", command=integrantes)
acerca_de.add_separator()
acerca_de.add_command(label="Curso", command=curso)

# --------------BOTON-----------------------------------------------------------------
Button(
    master, text="Buscar contacto", width=20, command=buscar_contacto, anchor=CENTER
).place(x=5, y=10)
# -----------------------------------------------------------------------------------
Button(master, text="Limpiar pantalla", width=20, command=limpiar, anchor=CENTER).place(
    x=5, y=200
)
# -----------------------------------------------------------------------------------
Button(master, text="Buscar todos", width=20, command=buscartodos, anchor=CENTER).place(
    x=5, y=100
)

w = Label(master, text="DATOS DE CONTACTO")
w.place(x=420, y=10)

w8 = Label(master, text="> FOTO DE PERFIL <")
w8.place(x=200, y=100)

db_conectado = connection_db()

if db_conectado == True:
    w6 = Label(master, text="Database Online", foreground="green")
    w6.place(x=525, y=280)
else:
    w7 = Label(master, text="Database Offline", foreground="red")
    w7.place(x=525, y=280)

master.mainloop()
