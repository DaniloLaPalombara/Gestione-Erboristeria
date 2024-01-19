from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneErboristeria.GestioneSistema.gestione import Gestore
from GestioneErboristeria.GestioneSistema.data import data

gestore = Gestore()


class Ui_RicercaMagazzino(object):
    def setupUi(self, Form):
        self.Frame = Form
        Form.setObjectName("Form")
        Form.resize(597, 376)
        self.Ricercaarticolobtn = QtWidgets.QPushButton(Form)
        self.Ricercaarticolobtn.setGeometry(QtCore.QRect(30, 290, 91, 41))
        self.Ricercaarticolobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ricercaarticolobtn.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.Ricercaarticolobtn.setIcon(icon)
        self.Ricercaarticolobtn.setObjectName("Ricercaarticolobtn")
        self.homebtn = QtWidgets.QPushButton(Form)
        self.homebtn.setGeometry(QtCore.QRect(450, 320, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 621, 391))
        self.frame.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/sfondomagazzino.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 310, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.ricercamagazzinotb = QtWidgets.QLineEdit(Form)
        self.ricercamagazzinotb.setGeometry(QtCore.QRect(140, 300, 191, 21))
        self.ricercamagazzinotb.setObjectName("ricercamagazzinotb")
        self.tableWidgetmagazzino = QtWidgets.QTableWidget(Form)
        self.tableWidgetmagazzino.setGeometry(QtCore.QRect(40, 30, 501, 221))
        self.tableWidgetmagazzino.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetmagazzino.setObjectName("tableWidgetmagazzino")
        self.tableWidgetmagazzino.setColumnCount(0)
        self.tableWidgetmagazzino.setRowCount(0)
        self.frame.raise_()
        self.Ricercaarticolobtn.raise_()
        self.homebtn.raise_()
        self.pushButton.raise_()
        self.ricercamagazzinotb.raise_()
        self.tableWidgetmagazzino.raise_()

        # Metodi di creazione e popolazione della widget list dei prodotti in magazzino
        self.creaListaProdotti()
        self.popolaMagazzino()

        # Metodi legati al click dei bottoni
        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToMagazzino)
        self.Ricercaarticolobtn.clicked.connect(self.ricercaArticolo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Ricercaarticolobtn.setText(_translate("Form", "  Ricerca"))
        self.homebtn.setText(_translate("Form", "Home"))

    # metodo che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che permette di tornare alla schermata del magazzino
    def returnToMagazzino(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.magazzino import Ui_Magazzino
        self.magazzino = QtWidgets.QFrame()
        self.ui = Ui_Magazzino()
        self.ui.setupUi(self.magazzino)
        self.magazzino.show()
        self.Frame.close()

    # metodo che permette di popolare la tabella con la lista dei prodotti in magazzino
    def creaListaProdotti(self):
        data.downloadMagazzino()
        self.tableWidgetmagazzino.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetmagazzino.setObjectName("tableWidget")
        self.tableWidgetmagazzino.setColumnCount(4)
        self.tableWidgetmagazzino.setRowCount(data.nFitoMagaz + data.nProdMagaz)
        for i in range(0, data.nFitoMagaz + data.nProdMagaz):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetmagazzino.setHorizontalHeaderItem(i, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetmagazzino.horizontalHeaderItem(0)
        item.setText(_translate("magazzino", "Prodotto"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(1)
        item.setText(_translate("magazzino", "Quantità"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(2)
        item.setText(_translate("magazzino", "Prezzo"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(3)
        item.setText(_translate("magazzino", "Codice"))
        self.tableWidgetmagazzino.horizontalHeader().setVisible(True)
        self.tableWidgetmagazzino.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetmagazzino.verticalHeader().setVisible(True)

    # metodo che permette di popolare la lista dei prodotti nel magazzino
    def popolaMagazzino(self):
        _translate = QtCore.QCoreApplication.translate
        listaTotaleProdotti = data.listaFitoMagazzino + data.listaProdottiMagazzino
        self.tableWidgetmagazzino.setRowCount(len(listaTotaleProdotti))

        for riga, prodotto in enumerate(listaTotaleProdotti):
            for colonna in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetmagazzino.setItem(riga, colonna, item)
                if colonna == 0:  # Nome del prodotto
                    nome = prodotto.get('nome', 'N/D')
                    item.setText(_translate("magazzino", nome))
                elif colonna == 1:  # Quantità
                    quantita = prodotto.get('quantita', 'N/D')
                    item.setText(_translate("magazzino", str(quantita)))
                elif colonna == 2:  # Prezzo
                    prezzo = prodotto.get('prezzo', 'N/D')
                    item.setText(_translate("magazzino", str(prezzo)))
                elif colonna == 3:  # Codice
                    codice = prodotto.get('codice', 'N/D')
                    item.setText(_translate("magazzino", codice))

    # metodo di ricerca di un articolo nella lista dei prodotti in magazzino
    def ricercaArticolo(self):
        param = self.ricercamagazzinotb.text()
        if (param == ""):
            self.popolaMagazzino()
            return
        else:
            prodottiRicercati = []
            for element in data.listaFitoMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            for element in data.listaProdottiMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
        self.popolaRicerca(prodottiRicercati)

    # metodo che restituisce nella tabella i prodotti ricercati
    def popolaRicerca(self, prodRicercati):
        self.tableWidgetmagazzino.clear()
        self.creaListaProdotti()
        item = self.tableWidgetmagazzino.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("magazzino", "Prodotto"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(1)
        item.setText(_translate("magazzino", "Quantità"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(2)
        item.setText(_translate("magazzino", "Prezzo"))
        item = self.tableWidgetmagazzino.horizontalHeaderItem(3)
        item.setText(_translate("magazzino", "Codice"))
        for riga in range(0, len(prodRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetmagazzino.setItem(riga, colonna, item)
                item = self.tableWidgetmagazzino.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("magazzino", prodRicercati[riga].nome))
                if (colonna == 1):
                    item.setText(_translate("magazzino", str(prodRicercati[riga].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("magazzino", str(prodRicercati[riga].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("magazzino", str(prodRicercati[riga].codice)))
