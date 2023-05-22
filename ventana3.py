import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QScrollArea, QTableWidget, QTableWidgetItem, \
    QPushButton, QApplication, QVBoxLayout
from PyQt5 import QtGui

from cliente import Cliente


class Ventana3(QMainWindow):

    #Hacer el metodo de construcción ventana:
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        # Creamos un abtributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        #poner titulo
        self.setWindowTitle("Usuarios Registrados")

        #poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.jpeg'))

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

        # Defínimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/travel.jpg')

        # Defínimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar los usuarios:
        self.usuarios = []

        # Recorremos el archivo, línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # Se para si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u
            U = Cliente(
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
            self.usuarios.append(U)

        # Cerramos el archivo:
        self.file.close()


      # En este punto tenemos la lista usuarios con todos los usuarios

        # Obtenemos el número de usuarios registrados:
        # Consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        # Establecemos la distribución de los eelmentos en vertical

        self.vertical = QVBoxLayout()

        #Hacemos un letrero
        self.letrero1 = QLabel()

        #Le escribimos el texto
        self.letrero1.setText("Usuarios registrados")

        #Asignamos tito de letra
        self.letrero1.setFont(QFont("Andale Mono",20))

        #Color de texto
        self.letrero1.setStyleSheet("Color: #C0C0C0")

        #Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Agregamos un espacio despues
        self.vertical.addStretch()

        # Creamos un scroll
        self.scrollArea = QScrollArea()

        # Hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        #Creamos una tabla
        self.tabla = QTableWidget()

        # Definimos el número de coumnas que tendra la tabla
        self.tabla.setColumnCount(11)

        #definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        #Definimos el texto de la cabecera
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        # Establecemos el número de filas
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos el layout vertical en el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Agregamos un espacio despues
        self.vertical.addStretch()

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

        # Metemos en el layout vertical el boton

        self.vertical.addWidget(self.botonVolver)


        # -------- OJO IMPORTANTE PONER AL FINAL --------

        # Indicamos que el layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())









