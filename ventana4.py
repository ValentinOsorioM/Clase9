import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore

from cliente import Cliente


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior

        self.cedulaUsuario = cedula


        #poner titulo
        self.setWindowTitle("Editar usuario")

        #poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.jpg'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # EstabLecemos el fondo principal:
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet("background-color: #FFDEAD;")

        #Establecemos la venta de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribució de los elemntos en layout horizontal
        self.horizontal = QHBoxLayout()

        # Le ponenos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ----- LAYOUT IZQUIERDO-------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos un letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Editar cliente")

        # Asignamos tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Color de texto
        self.letrero1.setStyleSheet("Color: #Black"
                                    "background-color: #FFDEAD;")

        # Agregamos el letrero en la primera linea
        self.ladoIzquierdo.addRow(self.letrero1)

        # letrero2
        self.letrero2 = QLabel()

        # establecemos el anchi del lanel
        self.letrero2.setFixedWidth(340)

        # le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        # Asignamos tito de letra
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemops color de textos y margenes
        self.letrero2.setStyleSheet("Color: #C0C0C0; margin-bottom: 40px;"
                                    "background-color: #FFDEAD;"
                                    "margin-bottom: 40px;"
                                    "margin-top:20px"
                                    "padding-bottom: 10px"
                                    "border: 2px solid #C0C0C0;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "norder-top: none;")

        # Agregamos el letrero en la primera linea
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usurio:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el possword2:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)


        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el fotmulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)


        #------ Boton editar----------

        # hacemos un boton para registrar los datos
        self.botonEditar = QPushButton("Editar")
        # establecemos el ancho del botton
        self.botonEditar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonEditar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        #----------- Boton limpiar -------------

        # hacemos el boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # agregamos los botones al layout izquierdo
        self.ladoIzquierdo.addRow(self.botonEditar, self.botonLimpiar)

        #--------- BOTON ELIMINAR-----------------

        # hacemos el boton para limpiar los datos
        self.botonEliminar = QPushButton("Eliminar")

        self.botonEliminar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonEliminar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        # agregamos los botones al layout izquierdo
        self.ladoIzquierdo.addRow(self.botonEliminar)

        # ---- BOTON VOLVER ----- #

        # Hacemos el botón para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del botón:
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008845;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        # Hacemos que el boton botonContinuar tenga su método:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Metemos en el layout principal el botonVolver
        self.ladoIzquierdo.addRow(self.botonVolver)


        # Agregamos el layout lado Izquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)


        # -----Layout derecho----
        # cramos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # se asigna la imagen solo a la izquierda
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # hacemos el letrero
        self.letrero3 = QLabel()

        # le escribimos el texto
        self.letrero3.setText("Editar Recuperar Contraseña")

        # Asignamos tipo de letra
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Color de texto
        self.letrero3.setStyleSheet("Color: #Black;")

        # agregamos el letrero a la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()

        # establecemos el ancho del label
        self.letrero4.setFixedWidth(400)

        # le escribimos el texto
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados "
                              "\ncon asteriscos con obligatorios.")

        # Asignamos tipo de letra
        self.letrero4.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de textos y margenes
        self.letrero4.setStyleSheet("Color: #black; "
                                    "background-color: #FF8C00"
                                    "margin-bottom: 40px"
                                    "margin-top: 20px"
                                    "padding-bottom: 10px"
                                    "border: 2px solid #FFFFFFF;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "norder-top: none;")

        # agregemos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.letrero4)

        # --1

        # hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta1)
        # hacemnos el campo para ingresar la pregunta 1
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        # agregemos el p1 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta1)

        # hacemos el letrero de la respuesta1
        self.labelRespuesta1 = QLabel("Respuesta de verificación1*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta1)
        # hacemnos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)
        # agregemos el p1 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta1)


        # --2
        # hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta2)
        # hacemnos el campo para ingresar la pregunta 2
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        # agregemos el p2 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el letrero de la respuesta2
        self.labelRespuesta2 = QLabel("Respuesta de verificación2*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta2)
        # hacemnos el campo para ingresar la respuesta 2
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        # agregemos el p2 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta2)

        # ---3
        # hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta3)
        # hacemnos el campo para ingresar la pregunta 3
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        # agregemos el p3 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el letrero de la respuesta3
        self.labelRespuesta3 = QLabel("Respuesta de verificación3*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta3)
        # hacemnos el campo para ingresar la respuesta 3
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)
        # agregemos el p3 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta3)

        #------

        # agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)



        # -------- OJO IMPORTANTE PONER AL FINAL --------

        # Indicamos que el layout principal del fondo es vertical
        self.fondo.setLayout(self.horizontal)


        #-----------------Construcción de ventana de dialogo ------------------

        # creamos la ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # creamos el boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # ventana modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # creamos el layout vertical
        self.vertical = QVBoxLayout()

        # creamos el label para los mensajes
        self.mensaje = QLabel("")

        # le pinesmos estilo al label mensaje
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # agregamos el label mensajes
        self.vertical.addWidget(self.mensaje)

        # agregamos las opciones de los botones
        self.vertical.addWidget(self.opciones)

        # establecemos el layout para la ventana
        self.ventanaDialogo.setLayout(self.vertical)

        # Llamamos al metodo para que se carguen los datos del formulario:
        self.cargar_datos()

    def accion_botonEditar(self):

        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = True

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        # validamos que los passwords sean iguales
        if (
                self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            self.ventanaDialogo.exec_()

        # Se valida para que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

        # escribimos el texto explicativo

            self.mensaje.setText("Debe seleccionar un usuario con documento valido!")

        # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        # si los datos estan correctos:
        if self.datosCorrectos:

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                #obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")
                # Se para si ya no hay más registros en el archivo
                if linea == '':
                    break

                 # Creamos un objeto tipo cliente llamado u
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

                # Metemos al objeto en la lista de usuarios:
                usuarios.append(u)

            #Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista de usuarios con todos los usuarios

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Llenamos la tabla
            for u in usuarios:
                # Comparamos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    # Guardamos los datos del formulario en las propiedas del usuario:

                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()

                    # Indicamos que encontramos el documento:

                    existeDocumento = True

                    #Paramos el for:
                    break
            # Si no existe un usuario con este documento
            if (
                    not existeDocumento
            ):
                # escribimos el texto explicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

            # abrimos el archivo en modo escritura datos en binario
            self.file = open('datos/clientes.txt', 'wb')

            # traer el texto de los QLineEdit y los agrega concatenandolos
            # para escribirlos en formato binario utf-8
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            # cerramos el archivo
            self.file.close()

            # Si existe un usuario con este documento
            # y si se edito correctamente
            if (
                   existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("Usuario actualizado correctamente!")

                #hacemos que la ventana se vea

                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.metodo_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()





    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonEliminar(self):
        #Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

        # controladores si vamos a eliminar
        self.eliminar = False

        # Se valida para que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # escribimos el texto explicativo
            self.mensaje.setText("Debe seleccionar un usuario con documento valido!")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        # si los datos estan correctos
        if self.datosCorrectos:


            # creamos la ventana de dialogo
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # definimos el tamaño de la ventana
            self.ventanaDialogoEliminar.resize(300, 150)

            # ventana modal
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # creamos el layout vertical
            self.verticalEliminar = QVBoxLayout()

            # creamos el label para los mensajes
            self.mensajeEliminar = QLabel("¿Está seguro que desea eliminar este registro de usuario?")

            # le pinesmos estilo al label mensaje
            self.mensajeEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

            # agregamos el label mensajes
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # Agregamos las opciones de aceptar y cancelar en la ventana de dialogo:
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            #Agregamos las opciones de los botones
            self.verticalEliminar.addWidget(self.opcionesBox)

            # Establecemos el layout para la ventana:
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            # hacemos que la ventana se vea
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # abrimos el archivo en modo escritura datos en binario
            self.file = open('datos/clientes.txt', 'rb')


            # Lista vacia para guardar los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                #obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")
                # Se para si ya no hay más registros en el archivo
                if linea == '':
                    break

                 # Creamos un objeto tipo cliente llamado u
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

                # Metemos al objeto en la lista de usuarios:
                usuarios.append(u)

            #Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista de usuarios con todos los usuarios

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Llenamos la tabla
            for u in usuarios:
                # Comparamos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    #eliminamos el usuario de la lista
                    usuarios.remove(u)
                    existeDocumento = True
                    # paramos el for
                    break

            # abrimos el archivo en modo escritura datos en binario
            self.file = open('datos/clientes.txt', 'wb')

            # traer el texto de los QLineEdit y los agrega concatenandolos
            # para escribirlos en formato binario utf-8
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            # cerramos el archivo
            self.file.close()

            # Si existe un usuario con este documento
            # y si se edito correctamente
            if (
                   existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("Usuario eliminado exitosamente!")

                #hacemos que la ventana se vea

                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.metodo_botonVolver()





    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()


    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):

        # Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar los usuarios:
        usuarios = []

        # Recorremos el archivo, línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # Se para si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            # Metemos el objeto en la lista de usuarios:
            usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista de usuarios con todos los usuarios

        # Variable para controlar si existe el documento:
        existeDocumento = False

        # Buscamos en la lista usuario por usuario si existe la cedula:
        for u in usuarios:
            # Comparamos el documento ingresado:
            # si corresponde con el documento, es el usuario correcto:
            if int(u.documento) == self.cedulaUsuario:
                # mostramos los datos en el formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                #Hacemos que el nombre no se pueda editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                #Hacemos que el docomento no se ueda editar
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                #Inicamos que encontramos el documento:

                existeDocumento = True

                #paramos el for:
                break

        #Si no existe un usuario con este documento
        if (
                not existeDocumento
        ):
            # escribimos el texto explicativo
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            #Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana4 = Ventana4()
    ventana4.show()
    sys.exit(app.exec_())

