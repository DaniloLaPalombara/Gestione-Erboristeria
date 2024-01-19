from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneErboristeria.GestioneSistema.gestione import Gestore

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()


class Ui_Magazzino(object):

    def setupUi(self, Magazzino):
        self.Frame = Magazzino
        Magazzino.setObjectName("Magazzino")
        Magazzino.resize(598, 380)
        self.Visualizzamagazzinobtn = QtWidgets.QPushButton(Magazzino)
        self.Visualizzamagazzinobtn.setGeometry(QtCore.QRect(90, 120, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Visualizzamagazzinobtn.setFont(font)
        self.Visualizzamagazzinobtn.setStyleSheet("border-radius: 25px;\n"
                                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Visualizzamagazzinobtn.setObjectName("Visualizzamagazzinobtn")
        self.EffettuaOrdinebtn = QtWidgets.QPushButton(Magazzino)
        self.EffettuaOrdinebtn.setGeometry(QtCore.QRect(310, 120, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.EffettuaOrdinebtn.setFont(font)
        self.EffettuaOrdinebtn.setStyleSheet("border-radius: 25px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.EffettuaOrdinebtn.setObjectName("EffettuaOrdinebtn")
        self.homebtn = QtWidgets.QPushButton(Magazzino)
        self.homebtn.setGeometry(QtCore.QRect(190, 270, 101, 31))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.Logoutbtn = QtWidgets.QPushButton(Magazzino)
        self.Logoutbtn.setGeometry(QtCore.QRect(300, 270, 101, 31))
        self.Logoutbtn.setStyleSheet("border-radius: 10px;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalogout.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.Logoutbtn.setIcon(icon1)
        self.Logoutbtn.setIconSize(QtCore.QSize(40, 40))
        self.Logoutbtn.setObjectName("Logoutbtn")
        self.frame = QtWidgets.QFrame(Magazzino)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 781, 541))
        self.frame.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/sfondomagazzino.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(Magazzino)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame.raise_()
        self.Visualizzamagazzinobtn.raise_()
        self.EffettuaOrdinebtn.raise_()
        self.homebtn.raise_()
        self.Logoutbtn.raise_()
        self.label.raise_()
        self.Logoutbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EffettuaOrdinebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Visualizzamagazzinobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.Logoutbtn.clicked.connect(self.returnToLogin)
        self.homebtn.clicked.connect(self.returnToHome)
        self.Visualizzamagazzinobtn.clicked.connect(self.openVisualizzaMagazzino)
        self.EffettuaOrdinebtn.clicked.connect(self.openSceltaFornitore)

        self.retranslateUi(Magazzino)
        QtCore.QMetaObject.connectSlotsByName(Magazzino)

    def retranslateUi(self, Magazzino):
        _translate = QtCore.QCoreApplication.translate
        Magazzino.setWindowTitle(_translate("Magazzino", "Form"))
        self.Visualizzamagazzinobtn.setText(_translate("Magazzino", "Visualizza Magazzino"))
        self.EffettuaOrdinebtn.setText(_translate("Magazzino", "Effettua Ordine"))
        self.homebtn.setText(_translate("Magazzino", "Home"))
        self.Logoutbtn.setText(_translate("Magazzino", "Logout"))
        self.label.setText(_translate("Magazzino", "Magazzino"))

    # metodo che permette di tornare alla schermata di login
    def returnToLogin(self):
        from GestioneErboristeria.Gui.GestioneLogin.login import Ui_Login
        self.login = QtWidgets.QFrame()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.Frame.close()

    # metodo che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che permette di visualizzare il magazzino
    def openVisualizzaMagazzino(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.ricercamagazzino import Ui_RicercaMagazzino
        self.visualizzaMagazzino = QtWidgets.QFrame()
        self.ui = Ui_RicercaMagazzino()
        self.ui.setupUi(self.visualizzaMagazzino)
        self.visualizzaMagazzino.show()
        self.Frame.close()

    # metodo che ti permette di aprire la schermata di scelta del fornitore
    def openSceltaFornitore(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.sceltafornitore import Ui_Fornitori
        self.scegliFornitore = QtWidgets.QFrame()
        self.ui = Ui_Fornitori()
        self.ui.setupUi(self.scegliFornitore)
        self.scegliFornitore.show()
        self.Frame.close()
