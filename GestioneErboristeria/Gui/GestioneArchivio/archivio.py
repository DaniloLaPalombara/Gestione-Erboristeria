from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from GestioneErboristeria.GestioneSistema.data import data
from GestioneErboristeria.GestioneSistema.gestione import Gestore

gestore = Gestore()


class Ui_Archivio(object):
    def setupUi(self, Form):
        self.Frame = Form
        Form.setObjectName("Form")
        Form.resize(827, 495)
        Form.setStyleSheet("")
        columns = ['Nome', 'Cognome', 'Cf', 'Email', 'Sesso', 'Indirizzo']
        self.Archivio = QtWidgets.QFrame(Form)
        self.Archivio.setGeometry(QtCore.QRect(0, -10, 831, 531))
        self.Archivio.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/archivio.jpg);")
        self.Archivio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Archivio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Archivio.setObjectName("Archivio")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 250, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.homebtn = QtWidgets.QPushButton(Form)
        self.homebtn.setGeometry(QtCore.QRect(710, 240, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 391, 161))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tableWidgetordini = QtWidgets.QTableWidget(Form)
        self.tableWidgetordini.setGeometry(QtCore.QRect(410, 40, 391, 161))
        self.tableWidgetordini.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetordini.setObjectName("tableWidgetordini")
        self.tableWidgetordini.setColumnCount(0)
        self.tableWidgetordini.setRowCount(0)
        self.tableWidgetclienti = QtWidgets.QTableWidget(Form)
        self.tableWidgetclienti.setGeometry(QtCore.QRect(10, 40, 391, 161))
        self.tableWidgetclienti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetclienti.setObjectName("tableWidgetclienti")
        self.tableWidgetclienti.setColumnCount(len(columns))
        self.tableWidgetclienti.setHorizontalHeaderLabels(columns)
        self.tableWidgetclienti.setRowCount(0)
        self.ricercaarchivioclientibtn = QtWidgets.QPushButton(Form)
        self.ricercaarchivioclientibtn.setGeometry(QtCore.QRect(210, 210, 91, 41))
        self.ricercaarchivioclientibtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchivioclientibtn.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.ricercaarchivioclientibtn.setIcon(icon1)
        self.ricercaarchivioclientibtn.setObjectName("ricercaarchivioclientibtn")
        self.ricercaarchivioordinibtn = QtWidgets.QPushButton(Form)
        self.ricercaarchivioordinibtn.setGeometry(QtCore.QRect(610, 210, 91, 41))
        self.ricercaarchivioordinibtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchivioordinibtn.setStyleSheet("border-radius: 10px;\n"
                                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.ricercaarchivioordinibtn.setIcon(icon1)
        self.ricercaarchivioordinibtn.setObjectName("ricercaarchivioordinibtn")
        self.ricercaarchivioclienti = QtWidgets.QLineEdit(Form)
        self.ricercaarchivioclienti.setGeometry(QtCore.QRect(10, 220, 191, 21))
        self.ricercaarchivioclienti.setObjectName("ricercaarchivioclienti")
        self.ricercaarchivioordini = QtWidgets.QLineEdit(Form)
        self.ricercaarchivioordini.setGeometry(QtCore.QRect(410, 220, 191, 21))
        self.ricercaarchivioordini.setObjectName("ricercaarchivioordini")
        self.ricercaarchiviovenditebtn = QtWidgets.QPushButton(Form)
        self.ricercaarchiviovenditebtn.setGeometry(QtCore.QRect(210, 450, 91, 41))
        self.ricercaarchiviovenditebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchiviovenditebtn.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.ricercaarchiviovenditebtn.setIcon(icon1)
        self.ricercaarchiviovenditebtn.setObjectName("ricercaarchiviovenditebtn")
        self.tableWidgetvendite = QtWidgets.QTableWidget(Form)
        self.tableWidgetvendite.setGeometry(QtCore.QRect(10, 280, 391, 161))
        self.tableWidgetvendite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetvendite.setObjectName("tableWidgetvendite")
        self.tableWidgetvendite.setColumnCount(0)
        self.tableWidgetvendite.setRowCount(0)
        self.ricercaarchiviovendite = QtWidgets.QLineEdit(Form)
        self.ricercaarchiviovendite.setGeometry(QtCore.QRect(10, 460, 191, 21))
        self.ricercaarchiviovendite.setObjectName("ricercaarchiviovendite")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.ricercaarchivioordinibtn.clicked.connect(self.ricercaOrdiniPerFornitore)
        self.ricercaarchiviovenditebtn.clicked.connect(self.ricercaVendite)
        self.ricercaarchivioclientibtn.clicked.connect(self.ricercaClienti)
        self.homebtn.clicked.connect(self.returnToHome)
        self.creaArchivioVendite()
        self.popolaVendite()
        self.creaArchivioOrdini()
        self.popolaOrdini()
        self.creaArchivioClienti()
        self.popolaClienti()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.homebtn.setText(_translate("Form", "Home"))
        self.label.setText(_translate("Form", "Archivio vendite"))
        self.ricercaarchivioclientibtn.setText(_translate("Form", "  Ricerca"))
        self.ricercaarchivioordinibtn.setText(_translate("Form", "  Ricerca"))
        self.ricercaarchiviovenditebtn.setText(_translate("Form", "  Ricerca"))
        self.label_4.setText(_translate("Form", "Archivio clienti"))
        self.label_2.setText(_translate("Form", "Archivio ordini"))

    # metodo che consente di tornare alla home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che gestisce la creazione di una tabella da popolare con tutti gli ordini effettuati
    def creaArchivioOrdini(self):
        data.downloadArchivioOrdini()
        self.tableWidgetordini.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetordini.setObjectName("tableWidget")
        self.tableWidgetordini.setColumnCount(4)
        self.tableWidgetordini.setRowCount(data.nOrdini)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetordini.setHorizontalHeaderItem(i, item)
        self.tableWidgetordini.horizontalHeader().setVisible(True)
        self.tableWidgetordini.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetordini.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetordini.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidgetordini.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fornitore"))
        item = self.tableWidgetordini.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Totale"))
        item = self.tableWidgetordini.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Data"))

    # metodo che popola la tabella con tutti gli ordini effettuati
    def popolaOrdini(self):
        _translate = QtCore.QCoreApplication.translate
        data.downloadArchivioOrdini()
        self.tableWidgetordini.setRowCount(len(data.archivioOrdini))
        for riga, ordine in enumerate(data.archivioOrdini):
            codice = ordine['codice']
            self.tableWidgetordini.setItem(riga, 0, QTableWidgetItem(_translate("Form", str(codice))))
            fornitore = ordine.get('fornitore', '')
            self.tableWidgetordini.setItem(riga, 1, QTableWidgetItem(_translate("Form", fornitore)))
            totale = ordine.get('totale', 0)
            self.tableWidgetordini.setItem(riga, 2, QTableWidgetItem(_translate("Form", f"{totale}€")))
            data_ordine = ordine.get('data', '')
            self.tableWidgetordini.setItem(riga, 3, QTableWidgetItem(_translate("Form", data_ordine)))

    # metodo che permette di ricercare gli ordini per fornitore
    def ricercaOrdiniPerFornitore(self):
        param = self.ricercaarchivioordini.text()
        ordiniRicercati = []
        if param == "":
            self.popolaOrdini()
            return
        for element in data.archivioOrdini:
            fornitore = element.get('fornitore', '')
            if param in fornitore:
                ordiniRicercati.append(element)

        self.popolaRicercaOrdini(ordiniRicercati)

    # metodo che aggiorna la tabella degli ordini in base alla ricerca effettuata
    def popolaRicercaOrdini(self, ordiniRicercati):
        self.tableWidgetordini.clear()
        self.creaArchivioOrdini()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(ordiniRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetordini.setItem(riga, colonna, item)
                item = self.tableWidgetordini.item(riga, colonna)
                if colonna == 0:
                    item.setText(_translate("Form", ordiniRicercati[riga]['codice']))
                if colonna == 1:
                    item.setText(_translate("Form", ordiniRicercati[riga]['fornitore']))
                if colonna == 2:
                    item.setText(_translate("Form", str(ordiniRicercati[riga]['totale'])[0:5] + "€"))
                if colonna == 3:
                    item.setText(_translate("Form", ordiniRicercati[riga]['data']))

    # metodo che gestisce la creazione di una tabella da popolare con tutte le vendite effettuate
    def creaArchivioVendite(self):
        data.downloadArchivioVendite()
        self.tableWidgetvendite.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetvendite.setObjectName("tableWidget")
        self.tableWidgetvendite.setColumnCount(4)
        self.tableWidgetvendite.setRowCount(data.nVendite)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetvendite.setHorizontalHeaderItem(i, item)
        self.tableWidgetvendite.horizontalHeader().setVisible(True)
        self.tableWidgetvendite.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetvendite.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetvendite.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidgetvendite.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Totale"))
        item = self.tableWidgetvendite.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Data"))

    # metodo che popola la tabella con tutte le vendite effettuate
    def popolaVendite(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(data.archivioVendite)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetvendite.setItem(riga, colonna, item)
                item = self.tableWidgetvendite.item(riga, colonna)
                if colonna == 0:
                    item.setText(_translate("Form", str(data.archivioVendite[riga]['codice'])))
                if colonna == 1:
                    item.setText(_translate("Form", str(data.archivioVendite[riga]['totale'])[0:5] + "€"))
                if colonna == 2:
                    item.setText(_translate("Form", data.archivioVendite[riga]['data']))

    # metodo che permette di ricercare le vendite
    def ricercaVendite(self):
        param = self.ricercaarchiviovendite.text()
        venditeRicercate = []
        if param == "":
            self.popolaVendite()
            return
        for element in data.archivioVendite:
            if param in element['data']:
                venditeRicercate.append(element)
        self.popolaRicercaVendite(venditeRicercate)

    # metodo che aggiorna la tabella delle vendite in base alla ricerca effettuata
    def popolaRicercaVendite(self, venditeRicercate):
        self.tableWidgetvendite.clear()
        self.creaArchivioVendite()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(venditeRicercate)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetvendite.setItem(riga, colonna, item)
                item = self.tableWidgetvendite.item(riga, colonna)
                if colonna == 0:
                    item.setText(_translate("Form", venditeRicercate[riga]['codice']))
                if colonna == 1:
                    item.setText(_translate("Form", str(venditeRicercate[riga]['totale'])[0:5] + "€"))
                if colonna == 2:
                    item.setText(_translate("Form", venditeRicercate[riga]['data']))

    # metodo che gestisce la creazione di una tabella da popolare con tutti i clienti
    def creaArchivioClienti(self):
        data.downloadArchivioClienti()
        self.tableWidgetclienti.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetclienti.setObjectName("tableWidget")
        self.tableWidgetclienti.setColumnCount(7)
        self.tableWidgetclienti.setRowCount(len(data.archivioClienti))
        for i in range(0, 7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetclienti.setHorizontalHeaderItem(i, item)
        self.tableWidgetclienti.horizontalHeader().setVisible(True)
        self.tableWidgetclienti.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetclienti.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetclienti.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidgetclienti.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cognome"))
        item = self.tableWidgetclienti.horizontalHeaderItem(2)
        item.setText(_translate("Form", "CF"))
        item = self.tableWidgetclienti.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Eta"))
        item = self.tableWidgetclienti.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidgetclienti.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Sesso"))
        item = self.tableWidgetclienti.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Indirizzo"))

    # metodo che popola la tabella con tutti i clienti
    def popolaClienti(self):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidgetclienti.setRowCount(len(data.archivioClienti))
        for riga, cliente in enumerate(data.archivioClienti):
            for colonna, chiave in enumerate(['nome', 'cognome', 'cf', 'eta', 'email', 'sesso', 'indirizzo']):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("Form", str(cliente.get(chiave, ''))))
                self.tableWidgetclienti.setItem(riga, colonna, item)

    # metodo che permette di ricercare i clienti per nome o cognome
    def ricercaClienti(self):
        param = self.ricercaarchivioclienti.text().strip().lower()
        clientiRicercati = []
        if param == "":
            self.popolaClienti()
            return
        for cliente in data.archivioClienti:
            nome_cliente = cliente.get('nome', '').lower()
            cognome_cliente = cliente.get('cognome', '').lower()

            if param in nome_cliente or param in cognome_cliente:
                clientiRicercati.append(cliente)

        self.popolaRicercaClienti(clientiRicercati)

    # metodo che aggiorna la tabella dei clienti in base alla ricerca effettuata
    def popolaRicercaClienti(self, clientiRicercati):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidgetclienti.setRowCount(len(clientiRicercati))
        for riga, cliente in enumerate(clientiRicercati):
            for colonna, chiave in enumerate(['nome', 'cognome', 'cf', 'eta', 'email', 'sesso', 'indirizzo']):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("Form", str(cliente.get(chiave, ''))))
                self.tableWidgetclienti.setItem(riga, colonna, item)
