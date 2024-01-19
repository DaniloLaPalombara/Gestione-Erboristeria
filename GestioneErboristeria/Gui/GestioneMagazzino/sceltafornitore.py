from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneErboristeria.GestioneSistema.gestione import Gestore

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Ui_Fornitori(object):

    def setupUi(self, Fornitori):
        self.Frame = Fornitori
        Fornitori.setObjectName("Fornitori")
        Fornitori.resize(723, 380)
        self.homebtn = QtWidgets.QPushButton(Fornitori)
        self.homebtn.setGeometry(QtCore.QRect(350, 320, 101, 31))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.label = QtWidgets.QLabel(Fornitori)
        self.label.setGeometry(QtCore.QRect(30, 10, 721, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Fornitori)
        self.pushButton.setGeometry(QtCore.QRect(270, 310, 61, 51))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Fornitori)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 781, 431))
        self.frame.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/sfondofornitori.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Herbabtn = QtWidgets.QRadioButton(Fornitori)
        self.Herbabtn.setGeometry(QtCore.QRect(20, 190, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Herbabtn.setFont(font)
        self.Herbabtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Herbabtn.setObjectName("Herbabtn")
        self.Abrosbtn = QtWidgets.QRadioButton(Fornitori)
        self.Abrosbtn.setGeometry(QtCore.QRect(20, 240, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Abrosbtn.setFont(font)
        self.Abrosbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Abrosbtn.setObjectName("Abrosbtn")
        self.frame.raise_()
        self.homebtn.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.Herbabtn.raise_()
        self.Abrosbtn.raise_()

        self.Herbabtn.clicked.connect(self.openFornitoreHerbalife)
        self.Abrosbtn.clicked.connect(self.openFornitoreAbros)
        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToMagazzino)

        self.retranslateUi(Fornitori)
        QtCore.QMetaObject.connectSlotsByName(Fornitori)

    def retranslateUi(self, Fornitori):
        _translate = QtCore.QCoreApplication.translate
        Fornitori.setWindowTitle(_translate("Fornitori", "Form"))
        self.homebtn.setText(_translate("Fornitori", "Home"))
        self.label.setText(_translate("Fornitori", "Scegli da quale fornitore acquistare i prodotti:"))
        self.Herbabtn.setText(_translate("Fornitori", "Herbalife"))
        self.Abrosbtn.setText(_translate("Fornitori", "Abros"))

    # metodo che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che permette di tornare al magazzino
    def returnToMagazzino(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.magazzino import Ui_Magazzino
        self.magazzino = QtWidgets.QFrame()
        self.ui = Ui_Magazzino()
        self.ui.setupUi(self.magazzino)
        self.magazzino.show()
        self.Frame.close()

    # metodo che ti permette di aprire la schermata di ordine da Herablife
    def openFornitoreHerbalife(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.fornitoreherbalife import Ui_herbalife
        self.herbalife = QtWidgets.QFrame()
        self.ui = Ui_herbalife()
        self.ui.setupUi(self.herbalife)
        self.herbalife.show()
        self.Frame.close()

    # metodo che ti permette di aprire la schermata di ordine da Abros
    def openFornitoreAbros(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.fornitoreAbros import Ui_abros
        self.abros = QtWidgets.QFrame()
        self.ui = Ui_abros()
        self.ui.setupUi(self.abros)
        self.abros.show()
        self.Frame.close()