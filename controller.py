from peewee import Value
import vista
import modulo
from tkinter.messagebox import *
import logging
from tkinter import *


def control_limpiar():

    """ funcion que limpia los campos en la pantalla principal """
    from_modulo_limpiar = modulo.limpiar()

    if from_modulo_limpiar == True:

        vista.e1_input.delete(0, END)
        vista.datos_contacto.delete(1.0, END)
        vista.w8.destroy()
        vista.w8 = Label(vista.master, text="> FOTO DE PERFIL <")
        vista.w8.place(x=200, y=100)
        vista.e1_input.delete(0, END)
        from_modulo_limpiar = False


def control_buscartodos(from_vista_todos):

    """ funcion que busca todos los contactos de la agenda, y los carga en la pantalla principal """
    import module_variable as mod_var

    mod_var.contacto_encontrado = []

    mod_var.func_modificar = False
    mod_var.contacto_search.clear()
    mod_var.buscartodos_boton = True
    texto = from_vista_todos
    texto = texto.upper()
    a = modulo.agenda.buscar(texto)

    # a = modulo.buscartodos(from_vista_todos)
    b = len(a)
    n = 0
    x = 0
    ready = False
    vista.datos_contacto.delete(1.0, END)

    if b == 0:
        mod_var.contacto_search.append("CONTACTO NO ENCONTRADO\n")

    if mod_var.contacto_search[0] != "CONTACTO NO ENCONTRADO\n":

        a = len(mod_var.contacto_search)

        while n < a:
            vista.datos_contacto.insert(
                INSERT, "Codigo: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Nombre: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Apellido: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Empresa: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Email: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Teléfono: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            if x == 6:
                vista.datos_contacto.insert(INSERT, "---*---*---<>---*---*---\n")
            x = 0

        vista.w8.destroy()
        vista.w8 = Label(vista.master, text="> FOTO DE PERFIL: NO DISPONIBLE <")
        vista.w8.place(x=165, y=100)
        mod_var.contacto_search.clear()

    else:
        vista.datos_contacto.insert(INSERT, "Info: {}\n".format("Agenda sin contactos"))
        vista.w8.destroy()
        vista.w8 = Label(vista.master, text="> FOTO DE PERFIL: NO DISPONIBLE <")
        vista.w8.place(x=165, y=100)
        mod_var.contacto_search.clear()


def control_buscarcontacto():

    """esta funcion busca un contacto específico dentro de la agenda, y lo muestra en la pantalla principal"""

    import module_variable as mod_var

    contacto_a_buscar = vista.e1_input.get()
    vista.datos_contacto.delete(1.0, END)

    mod_var.func_modificar = False
    vista.w8.destroy()
    mod_var.contacto_search.clear()
    mod_var.buscartodos_boton = False
    texto = contacto_a_buscar
    texto = texto.upper()
    contacto = modulo.agenda.buscar(texto)

    if mod_var.no_encontrado == 0:
        vista.datos_contacto.insert(INSERT, "---*---*---<>---*---*---\n")
        vista.datos_contacto.insert(INSERT, "CONTACTO NO ENCONTRADO\n")
    else:
        n = 0
        while n < 6:
            mod_var.contacto_search.append(contacto[n])
            n += 1

        if mod_var.buscartodos_boton == False:
            mod_var.image_64_encode = contacto[6]
            if mod_var.image_64_encode != b"":
                modulo.foto_perfil_decode()
        n = 0
        x = 0
        ready = False
        a = len(mod_var.contacto_search)
        while n < a:
            vista.datos_contacto.insert(
                INSERT, "Codigo: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Nombre: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Apellido: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Empresa: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Email: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            vista.datos_contacto.insert(
                INSERT, "Teléfono: {}\n".format(mod_var.contacto_search[n])
            )
            n += 1
            x += 1
            if x == 6:
                vista.datos_contacto.insert(INSERT, "---*---*---<>---*---*---\n")
            x = 0
    if (
        (mod_var.func_modificar == False)
        & (mod_var.no_encontrado == 1)
        & (mod_var.image_64_encode != b"")
        & (mod_var.encontrado < 2)
    ):
        vista.w8 = Label(vista.master, image=mod_var.render)
        vista.w8.image = mod_var.render
        vista.w8.place(x=180, y=60)
        mod_var.contacto_search.clear()
    else:
        vista.w8 = Label(vista.master, text="> FOTO DE PERFIL: NO DISPONIBLE <")
        vista.w8.place(x=165, y=100)


def control_buscar_editar():

    """ esta funcion se utiliza para buscar el contacto deseado cuando se quiere editar un contacto """

    import module_variable as mod_var

    global nombre_aux
    global apellido_aux
    global empresa_aux
    global email_aux
    global movil_aux
    global image_64_encode
    global image_64_encode_aux

    texto = vista.contacto_buscar.get()

    vista.datos_nombre.delete(0, END)
    vista.datos_apellido.delete(0, END)
    vista.datos_email.delete(0, END)
    vista.datos_empresa.delete(0, END)
    vista.datos_movil.delete(0, END)
    texto = vista.contacto_buscar.get()

    mod_var.func_modificar = True
    texto = texto.upper()
    contacto = modulo.agenda.buscar(texto)

    """ aca imprime datos de la pantalla del menú editar """
    if mod_var.no_encontrado == 0:
        vista.datos_nombre.insert(INSERT, "CONTACTO NO ENCONTRADO")
        vista.datos_apellido.insert(INSERT, "CONTACTO NO ENCONTRADO")
        vista.datos_empresa.insert(INSERT, "CONTACTO NO ENCONTRADO")
        vista.datos_email.insert(INSERT, "CONTACTO NO ENCONTRADO")
        vista.datos_movil.insert(INSERT, "CONTACTO NO ENCONTRADO")

    elif mod_var.total_encontrados > 1:
        showinfo(
            "@Ingreso de datos",
            "Ingresar otro tipo de dato para buscar el contacto, ya que existen 2 o más usuarios con el mismo dato",
        )
        vista.datos_nombre.delete(0, END)
        vista.datos_apellido.delete(0, END)
        vista.datos_email.delete(0, END)
        vista.datos_empresa.delete(0, END)
        vista.datos_movil.delete(0, END)
        vista.contacto_buscar.delete(0, END)
        vista.win_modificar.focus_set()
    else:
        mod_var.codigo = contacto[0]
        vista.datos_nombre.insert(INSERT, contacto[1])
        vista.datos_apellido.insert(INSERT, contacto[2])
        vista.datos_empresa.insert(INSERT, contacto[3])
        vista.datos_email.insert(INSERT, contacto[4])
        vista.datos_movil.insert(INSERT, contacto[5])
        nombre_aux = vista.datos_nombre.get()
        apellido_aux = vista.datos_apellido.get()
        empresa_aux = vista.datos_empresa.get()
        email_aux = vista.datos_email.get()
        movil_aux = vista.datos_movil.get()
        mod_var.image_64_encode = contacto[6]
        image_64_encode_aux = mod_var.image_64_encode

        if mod_var.image_64_encode != b"":
            modulo.foto_perfil_decode()

    if (
        (mod_var.func_modificar == True)
        & (mod_var.no_encontrado == 1)
        & (mod_var.image_64_encode != b"")
        & (mod_var.total_encontrados < 2)
    ):
        vista.w9.destroy()
        vista.w9 = Label(vista.win_modificar, image=mod_var.render)
        vista.w9.image = mod_var.render
        vista.w9.place(x=10, y=260)
    else:
        vista.w9.destroy()
        vista.w9 = Label(vista.win_modificar, text="> FOTO DE PERFIL: NO DISPONIBLE <")
        vista.w9.place(x=10, y=310)


def control_pasaje_eliminar():

    """esta funcion se emplea para borrar un contacto de la base de datos"""
    import module_variable as mod_var

    nombre = vista.datos_nombre.get()
    apellido = vista.datos_apellido.get()
    empresa = vista.datos_empresa.get()
    email = vista.datos_email.get()
    movil = vista.datos_movil.get()
    mod_var.var_eliminar = True

    if vista.contacto_buscar.get() != "":
        a = modulo.agenda.eliminar(
            nombre, apellido, empresa, email, movil, mod_var.codigo
        )
        vista.win_modificar.destroy()
    else:
        showinfo("@Eliminar", "Ingrese los datos del contacto a eliminar")
        vista.win_modificar.focus_set()


def control_clear_window():

    """esta funcion se emplea limpiar los campos en la pantalla del menu editar"""
    global w9
    from_modulo_limpiar_editar = modulo.clear_window()

    if from_modulo_limpiar_editar == True:

        vista.datos_nombre.delete(0, END)
        vista.datos_apellido.delete(0, END)
        vista.datos_email.delete(0, END)
        vista.datos_empresa.delete(0, END)
        vista.datos_movil.delete(0, END)
        vista.contacto_buscar.delete(0, END)
        vista.w9.destroy()
        vista.w9 = Label(vista.win_modificar, text=">FOTO_PERFIL<")
        vista.w9.place(x=10, y=310)
        from_modulo_limpiar_editar = False


def control_exportar():

    """esta funcion se emplea para exportar la agenda en formatos csv, pdf, json, xml"""
    modulo.exportar()


def control_pasaje_regex():

    """ esta funcion realiza el chequeo de los datos ingresados a través de una expresión regular,​ también conocida como regex"""
    import re
    import vista as vist_mod
    import module_variable as mod_var

    global nombre_aux
    global apellido_aux
    global empresa_aux
    global email_aux
    global movil_aux
    global image_64_encode_aux

    validez_campos_1 = False
    validez_campos_2 = False
    validez_campos_3 = False
    validez_campos_4 = False
    validez_campos_5 = False
    mod_var.actualizar_imagen = False

    if mod_var.ventana_open_editar == True:
        mod_var.dato_ingresado = vista.contacto_buscar.get()

    if mod_var.var1.get() == True:
        modulo.foto_perfil_alta()

    if mod_var.var2.get() == True:
        modulo.foto_perfil_alta()
        mod_var.actualizar_imagen = True

    if mod_var.dato_ingresado != "" or mod_var.ventana_open == True:

        mod_var.ventana_open_editar = False

        nombre = vist_mod.datos_nombre.get()
        apellido = vist_mod.datos_apellido.get()
        empresa = vist_mod.datos_empresa.get()
        email = vist_mod.datos_email.get()
        movil = vist_mod.datos_movil.get()
        nombre = nombre.upper()
        apellido = apellido.upper()
        empresa = empresa.upper()
        email = email.upper()

        reg_empresa = "[A-Za-z0-9]"
        reg_nom_apellido = "[a-zA-Z ]{2,254}"
        reg_telefono = "(\+54|54)?[ -]*([0-9]{10}$)"
        reg_mail = re.compile(
            r"^((\w[^\W]+)[\.\-]?){1,}\@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
        )

        """ script que valida el nombre (debe de contener solo letras y al menos 2 caracteres)"""

        if re.match(reg_nom_apellido, nombre):
            validez_campos_1 = True
        else:
            showinfo(
                "@nombre",
                "El nombre debe de contener solo letras y al menos 2 caracteres",
            )
            validez_campos_1 = False

            if mod_var.func_modificar == True:
                if mod_var.ventana_open_editar == True:
                    vist_mod.win_modificar.focus_set()
            else:
                if mod_var.ventana_open == True:
                    vist_mod.win_alta.focus_set()

        """ script que valida Apellido (debe de contener solo letras y al menos 2 caracteres) """

        if re.match(reg_nom_apellido, apellido):
            validez_campos_2 = True
        else:
            showinfo(
                "@nombre",
                "El Apellido debe de contener solo letras y al menos 2 caracteres",
            )
            validez_campos_2 = False

            if mod_var.func_modificar == True:
                if mod_var.ventana_open_editar == True:
                    vist_mod.win_modificar.focus_set()
            else:
                if mod_var.ventana_open == True:
                    vist_mod.win_alta.focus_set()

        """ script que valida que el telefono contenga 10 caracteres numericos"""

        if re.match(reg_telefono, movil):
            validez_campos_3 = True
        else:
            showinfo("@Teléfono", "El telefono debe de contener 10 digitos numericos")
            validez_campos_3 = False

            if mod_var.func_modificar == True:
                if mod_var.ventana_open_editar == True:
                    vist_mod.win_modificar.focus_set()
            else:
                if mod_var.ventana_open == True:
                    vist_mod.win_alta.focus_set()

        """ script que valida Empresa (puede contener letras y números) """

        if re.match(reg_empresa, empresa):
            validez_campos_4 = True
        else:
            showinfo("@Empresa", "Ingrese el nombre de la empresa")
            validez_campos_4 = False

            if mod_var.func_modificar == True:
                if mod_var.ventana_open_editar == True:
                    vist_mod.win_modificar.focus_set()
            else:
                if mod_var.ventana_open == True:
                    vist_mod.win_alta.focus_set()

        """ script que valida el correo electrónico """

        if re.match(reg_mail, email):
            validez_campos_5 = True
        else:
            showinfo("@Email", "Ingrese nuevamente la dirección de correo electrónico")
            validez_campos_5 = False

            if mod_var.func_modificar == True:
                if mod_var.ventana_open_editar == True:
                    vist_mod.win_modificar.focus_set()
            else:
                if mod_var.ventana_open == True:
                    vist_mod.win_alta.focus_set()

        if (
            mod_var.func_modificar
            == True & validez_campos_1
            == True & validez_campos_2
            == True & validez_campos_3
            == True & validez_campos_4
            == True & validez_campos_5
            == True
        ):
            if (
                nombre != nombre_aux
                or apellido != apellido_aux
                or empresa != empresa_aux
                or email != email_aux
                or movil != movil_aux
            ):
                a = modulo.agenda.actualizar(
                    nombre,
                    apellido,
                    empresa,
                    email,
                    movil,
                    mod_var.codigo,
                    nombre_aux,
                    apellido_aux,
                    empresa_aux,
                    email_aux,
                    movil_aux,
                    image_64_encode_aux,
                )
                vista.win_modificar.destroy()
            else:
                showinfo(
                    "@Actualizar",
                    "Los registros son los mismos. Ingrese nuevos registros",
                )
                vista.win_modificar.focus_set()
                # mod_var.dato_ingresado = ""
        elif (
            validez_campos_1
            == True & validez_campos_2
            == True & validez_campos_3
            == True & validez_campos_4
            == True & validez_campos_5
            == True
        ):

            a = modulo.agenda.cargar_contacto(
                nombre, apellido, empresa, email, movil, mod_var.image_64_encode
            )
            vista.win_alta.destroy()
            mod_var.ventana_open = False

    else:
        showinfo("@Eliminar", "Ingrese los datos del contacto a actualizar")
        vista.win_modificar.focus_set()
        mod_var.ventana_open_editar = False
        mod_var.ventana_open = False
        mod_var.func_modificar = False
