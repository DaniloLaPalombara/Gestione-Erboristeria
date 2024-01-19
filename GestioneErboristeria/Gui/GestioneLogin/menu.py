from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneErboristeria.GestioneSistema.gestione import Gestore
from GestioneErboristeria.Gui.GestioneMagazzino.magazzino import Ui_Magazzino

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()


class Ui_Menu(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1109, 731)
        Form.setMinimumSize(QtCore.QSize(1109, 731))
        Form.setMaximumSize(QtCore.QSize(1109, 16777215))
        Form.setStyleSheet("")
        self.form = Form
        self.cassabtn = QtWidgets.QPushButton(Form)
        self.cassabtn.setGeometry(QtCore.QRect(150, 150, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cassabtn.setFont(font)
        self.cassabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cassabtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius: 25px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconacassa.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.cassabtn.setIcon(icon)
        self.cassabtn.setIconSize(QtCore.QSize(90, 90))
        self.cassabtn.setObjectName("cassabtn")
        self.archiviobtn = QtWidgets.QPushButton(Form)
        self.archiviobtn.setGeometry(QtCore.QRect(150, 340, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.archiviobtn.setFont(font)
        self.archiviobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.archiviobtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0995025 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius: 25px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconaarchivio.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.archiviobtn.setIcon(icon1)
        self.archiviobtn.setIconSize(QtCore.QSize(90, 90))
        self.archiviobtn.setObjectName("archiviobtn")
        self.magazzinobtn = QtWidgets.QPushButton(Form)
        self.magazzinobtn.setGeometry(QtCore.QRect(690, 150, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.magazzinobtn.setFont(font)
        self.magazzinobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.magazzinobtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.975124 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius: 25px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconamagazzino.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.magazzinobtn.setIcon(icon2)
        self.magazzinobtn.setIconSize(QtCore.QSize(90, 90))
        self.magazzinobtn.setObjectName("magazzinobtn")
        self.calendariobtn = QtWidgets.QPushButton(Form)
        self.calendariobtn.setGeometry(QtCore.QRect(690, 340, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calendariobtn.setFont(font)
        self.calendariobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendariobtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius: 25px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/calendario2.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.calendariobtn.setIcon(icon3)
        self.calendariobtn.setIconSize(QtCore.QSize(90, 90))
        self.calendariobtn.setObjectName("calendariobtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 50, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 1141, 751))
        self.frame.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/Menu.jpeg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logoutbtn = QtWidgets.QPushButton(Form)
        self.logoutbtn.setGeometry(QtCore.QRect(690, 540, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logoutbtn.setFont(font)
        self.logoutbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutbtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius: 25px;")
        self.logoutbtn.setInputMethodHints(QtCore.Qt.ImhNone)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalogout.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.logoutbtn.setIcon(icon4)
        self.logoutbtn.setIconSize(QtCore.QSize(90, 90))
        self.logoutbtn.setObjectName("logoutbtn")
        self.frame.raise_()
        self.cassabtn.raise_()
        self.archiviobtn.raise_()
        self.magazzinobtn.raise_()
        self.calendariobtn.raise_()
        self.label.raise_()
        self.logoutbtn.raise_()

        self.logoutbtn.clicked.connect(self.returnToLogin)
        self.magazzinobtn.clicked.connect(self.openMagazzino)
        self.archiviobtn.clicked.connect(self.openArchivio)
        self.cassabtn.clicked.connect(self.openCassa)
        self.calendariobtn.clicked.connect(self.openAppuntamenti)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cassabtn.setText(_translate("Form", "    Cassa"))
        self.archiviobtn.setText(_translate("Form", "      Archivio"))
        self.magazzinobtn.setText(_translate("Form", "    Magazzino"))
        self.calendariobtn.setText(_translate("Form", "   Calendario"))
        self.label.setText(_translate("Form", "Benvenuto"))
        self.logoutbtn.setText(_translate("Form", "  Logout"))

    # metodo che permette di tornare al login
    def returnToLogin(self):
        from GestioneErboristeria.Gui.GestioneLogin.login import Ui_Login
        self.login = QtWidgets.QFrame()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.form.close()

    # metodo che permette di aprire il magazzino
    def openMagazzino(self):
        self.magazzino = QtWidgets.QFrame()
        self.ui = Ui_Magazzino()
        self.ui.setupUi(self.magazzino)
        self.magazzino.show()
        self.form.close()

    # metodo che permette di aprire la cassa
    def openCassa(self):
        from GestioneErboristeria.Gui.GestioneCassa.cassa import Ui_Cassa
        self.cassa = QtWidgets.QFrame()
        self.ui = Ui_Cassa()
        self.ui.setupUi(self.cassa)
        self.cassa.show()
        self.form.close()

    # metodo che permette di aprire l'archivio
    def openArchivio(self):
        from GestioneErboristeria.Gui.GestioneArchivio.archivio import Ui_Archivio
        self.archivio = QtWidgets.QFrame()
        self.ui = Ui_Archivio()
        self.ui.setupUi(self.archivio)
        self.archivio.show()
        self.form.close()

    # metodo che permette di aprire la schermata degli appuntamenti
    def openAppuntamenti(self):
        from GestioneErboristeria.Gui.GestioneAppuntamenti.calendario import Ui_DialogCalendario
        self.appuntamento = QtWidgets.QFrame()
        self.ui = Ui_DialogCalendario()
        self.ui.setupUi(self.appuntamento)
        self.appuntamento.show()
        self.form.close()
