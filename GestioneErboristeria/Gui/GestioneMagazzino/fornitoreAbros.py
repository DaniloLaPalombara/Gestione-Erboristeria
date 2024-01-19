from datetime import date
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneErboristeria.GestioneSistema.data import data
from GestioneErboristeria.GestioneSistema.gestione import Gestore

gestore = Gestore()


class Ui_abros(object):
    nProdSelezionati = 0
    prodSelezionati = []
    totale = []

    def setupUi(self, abros):
        self.Frame = abros
        abros.setObjectName("abros")
        abros.resize(937, 587)
        self.label_4 = QtWidgets.QLabel(abros)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.ricercafornitorebtn = QtWidgets.QPushButton(abros)
        self.ricercafornitorebtn.setGeometry(QtCore.QRect(30, 370, 91, 41))
        self.ricercafornitorebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercafornitorebtn.setStyleSheet("border-radius: 10px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.ricercafornitorebtn.setIcon(icon)
        self.ricercafornitorebtn.setObjectName("ricercafornitorebtn")
        self.lineEdit = QtWidgets.QLineEdit(abros)
        self.lineEdit.setGeometry(QtCore.QRect(140, 380, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.codicele = QtWidgets.QLineEdit(abros)
        self.codicele.setGeometry(QtCore.QRect(70, 500, 131, 20))
        self.codicele.setObjectName("codicele")
        self.label = QtWidgets.QLabel(abros)
        self.label.setGeometry(QtCore.QRect(50, 450, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.quantitaprodsb = QtWidgets.QSpinBox(abros)
        self.quantitaprodsb.setGeometry(QtCore.QRect(240, 500, 42, 22))
        self.quantitaprodsb.setObjectName("quantitaprodsb")
        self.carrellobtn = QtWidgets.QPushButton(abros)
        self.carrellobtn.setGeometry(QtCore.QRect(290, 530, 131, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon1)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.label_3 = QtWidgets.QLabel(abros)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(abros)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 951, 601))
        self.frame.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/abros.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(abros)
        self.pushButton.setGeometry(QtCore.QRect(700, 510, 61, 51))
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
        self.homebtn = QtWidgets.QPushButton(abros)
        self.homebtn.setGeometry(QtCore.QRect(780, 520, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.homebtn.setIcon(icon3)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.tableWidgetlist = QtWidgets.QTableWidget(abros)
        self.tableWidgetlist.setGeometry(QtCore.QRect(20, 70, 451, 231))
        self.tableWidgetlist.setObjectName("tableWidgetlist")
        self.tableWidgetlist.setColumnCount(0)
        self.tableWidgetlist.setRowCount(0)
        self.tableWidgetcarrello = QtWidgets.QTableWidget(abros)
        self.tableWidgetcarrello.setGeometry(QtCore.QRect(480, 70, 451, 231))
        self.tableWidgetcarrello.setObjectName("tableWidgetcarrello")
        self.tableWidgetcarrello.setColumnCount(0)
        self.tableWidgetcarrello.setRowCount(0)
        self.acquistabtn = QtWidgets.QPushButton(abros)
        self.acquistabtn.setGeometry(QtCore.QRect(790, 320, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon4)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.frame.raise_()
        self.label_4.raise_()
        self.ricercafornitorebtn.raise_()
        self.lineEdit.raise_()
        self.codicele.raise_()
        self.label.raise_()
        self.quantitaprodsb.raise_()
        self.carrellobtn.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.homebtn.raise_()
        self.tableWidgetlist.raise_()
        self.tableWidgetcarrello.raise_()
        self.acquistabtn.raise_()

        self.creaListaProdotti()
        self.popolaListaProdotti()

        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToFornitori)
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        self.acquistabtn.clicked.connect(self.chiudiOrdine)
        self.ricercafornitorebtn.clicked.connect(self.ricercaArticolo)

        self.prodSelezionati.clear()
        self.totale.clear()

        self.retranslateUi(abros)
        QtCore.QMetaObject.connectSlotsByName(abros)

    def retranslateUi(self, abros):
        _translate = QtCore.QCoreApplication.translate
        abros.setWindowTitle(_translate("abros", "Form"))
        self.label_4.setText(_translate("abros", "Lista prodotti:"))
        self.ricercafornitorebtn.setText(_translate("abros", "  Ricerca"))
        self.label.setText(_translate("abros", "Inserisci codice e quantità da comprare"))
        self.carrellobtn.setText(_translate("abros", "Metti nel carrello"))
        self.label_3.setText(_translate("abros", "Carrello:"))
        self.homebtn.setText(_translate("abros", "Home"))
        self.acquistabtn.setText(_translate("abros", "  Acquista"))

    # metodo che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    # metodo che permette di tornare alla schermata di scelta fornitore
    def returnToFornitori(self):
        from GestioneErboristeria.Gui.GestioneMagazzino.sceltafornitore import Ui_Fornitori
        self.fornitori = QtWidgets.QFrame()
        self.ui = Ui_Fornitori()
        self.ui.setupUi(self.fornitori)
        self.fornitori.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    # metodo che permette di popolare la tabrlla con la lista dei prodotti del fornitore
    def creaListaProdotti(self):
        data.downloadFornitore()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(4)
        self.tableWidgetlist.setRowCount(data.nFitoForn + data.nProdForn)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)
        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    # metodo che permette di popolare la lista dei prodotti del fornitore
    def popolaListaProdotti(self):
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("abros", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("abros", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("abros", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("abros", "Codice"))
        for riga in range(len(data.listaFitoFornitore)):
            for colonna in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)

                prodotto = data.listaFitoFornitore[riga]

                if colonna == 0:
                    item.setText(_translate("abros", prodotto.get('nome')))
                elif colonna == 1:
                    item.setText(_translate("abros", str(prodotto.get('quantita'))))
                elif colonna == 2:
                    item.setText(_translate("abros", str(prodotto.get('prezzo'))))
                elif colonna == 3:
                    item.setText(_translate("abros", prodotto.get('codice')))

        for riga in range(data.nFitoForn, data.nFitoForn + data.nProdForn):
            for colonna in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)

                prodotto = data.listaProdottiFornitore[riga - data.nFitoForn]

                if colonna == 0:
                    item.setText(_translate("abros", prodotto.get('nome')))
                elif colonna == 1:
                    item.setText(_translate("abros", str(prodotto.get('quantita'))))
                elif colonna == 2:
                    item.setText(_translate("abros", str(prodotto.get('prezzo'))))
                elif colonna == 3:
                    item.setText(_translate("abros", prodotto.get('codice')))

    # metodo che effettua la ricerca di un articolo nella lista dei prodotti fornitore
    def ricercaArticolo(self):
        param = self.lineEdit.text().lower()
        prodottiRicercati = []
        for prodotto in data.listaFitoFornitore:
            if param in prodotto['nome'].lower() or param in prodotto['codice'].lower():
                prodottiRicercati.append(prodotto)
        for prodotto in data.listaProdottiFornitore:
            if param in prodotto['nome'].lower() or param in prodotto['codice'].lower():
                prodottiRicercati.append(prodotto)

        self.popolaRicerca(prodottiRicercati)

    # metodo che restituisce i prodotti ricercati
    def popolaRicerca(self, prodRicercati):
        self.tableWidgetlist.clear()
        self.creaListaProdotti()
        _translate = QtCore.QCoreApplication.translate
        headers = ["Prodotto", "Quantità", "Prezzo", "Codice"]
        for i, header in enumerate(headers):
            item = self.tableWidgetlist.horizontalHeaderItem(i)
            item.setText(_translate("abros", header))
        for riga, prodotto in enumerate(prodRicercati):
            for colonna in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                if colonna == 0:
                    item.setText(_translate("abros", prodotto['nome']))
                elif colonna == 1:
                    item.setText(_translate("abros", str(prodotto['quantita'])))
                elif colonna == 2:
                    item.setText(_translate("abros", str(prodotto['prezzo'])))
                elif colonna == 3:
                    item.setText(_translate("abros", prodotto['codice']))

    # metodo che crea la lista di prodotti nel carrello da acquistare
    def creaCarrello(self):
        self.tableWidgetcarrello.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetcarrello.setObjectName("tableWidget")
        self.tableWidgetcarrello.setColumnCount(4)
        self.tableWidgetcarrello.setRowCount(data.nFitoForn + data.nProdForn)
        for x in range(data.nFitoForn + data.nProdForn):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setHorizontalHeaderItem(x, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetcarrello.horizontalHeaderItem(0)
        item.setText(_translate("abros", "Prodotto"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(1)
        item.setText(_translate("abros", "Quantità"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(2)
        item.setText(_translate("abros", "Prezzo"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(3)
        item.setText(_translate("abros", "Codice"))
        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    # metodo che permette di selezionare un prodotto da inserire nel carrello
    def selezionaProdotto(self):
        from tkinter import messagebox
        param = self.codicele.text()
        if self.quantitaprodsb.value() == 0:
            messagebox.showinfo("Errore", "Inserisci la quantità da acquistare")
            return
        for element in data.listaFitoFornitore + data.listaProdottiFornitore:
            if param == element['codice']:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)
                if self.quantitaprodsb.value() <= element['quantita']:
                    element['quantita'] = self.quantitaprodsb.value()
                    for x in range(nProdSelezionati):
                        if param == self.prodSelezionati[x]['codice']:
                            elemrimosso = self.prodSelezionati.pop(x)
                            messagebox.showinfo("Imprevisto",
                                                "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                                                " a favore dell'inserimento del prodotto appena selezionato")
                            self.creaCarrello()
                            self.modificaCarrello(x, elemrimosso)
                            return

                    self.creaCarrello()
                    self.popolaCarrello(nProdSelezionati)
                    return
                else:
                    self.prodSelezionati.pop(-1)
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della quantita dell'articolo")
                    return

        messagebox.showinfo("Errore", "Inserisci il codice corretto")
        return

    # metodo che popola il carrello con i prodotti selezionati
    def popolaCarrello(self, nProdSelezionati):
        _translate = QtCore.QCoreApplication.translate
        # Assumi che self.prodSelezionati sia una lista di dizionari
        prodotto = self.prodSelezionati[nProdSelezionati]
        for colonna in range(4):  # Numero di colonne
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(nProdSelezionati, colonna, item)
            if colonna == 0:  # Nome del prodotto
                item.setText(_translate("abros", prodotto['nome']))
            elif colonna == 1:  # Quantità
                item.setText(_translate("abros", str(self.quantitaprodsb.value())))
            elif colonna == 2:  # Prezzo
                item.setText(_translate("abros", str(prodotto['prezzo'])))
            elif colonna == 3:  # Codice
                item.setText(_translate("abros", prodotto['codice']))

        self.totale.append(prodotto['prezzo'] * self.quantitaprodsb.value())

    # metodo che permette di modificare il carrello e di rimuovere quelli selezionati
    def modificaCarrello(self, riga, elemrimosso):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(4):  # Numero di colonne
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(riga, colonna, item)
            if colonna == 0:  # Nome del prodotto
                item.setText(_translate("abros", elemrimosso['nome']))
            elif colonna == 1:  # Quantità
                item.setText(_translate("abros", str(self.quantitaprodsb.value())))
            elif colonna == 2:  # Prezzo
                item.setText(_translate("abros", str(elemrimosso['prezzo'])))
            elif colonna == 3:  # Codice
                item.setText(_translate("abros", elemrimosso['codice']))

        self.totale[riga] = elemrimosso['prezzo'] * self.quantitaprodsb.value()

    # metodo che permette di chiudere l'ordine di prodotti dalla lista fornitori
    def chiudiOrdine(self):
        from tkinter import messagebox
        if not self.prodSelezionati:
            messagebox.showinfo("Errore", "Inserisci almeno un prodotto nel carrello")
            return

        data.downloadMagazzino()
        data.downloadFornitore()

        for element in self.prodSelezionati:
            check_in_magazzino = False
            for prodottoM in data.listaProdottiMagazzino:
                if element['codice'] == prodottoM['codice']:
                    prodottoM['quantita'] += element['quantita']
                    check_in_magazzino = True
                    break

            if not check_in_magazzino:
                new_item = element.copy()
                new_item['quantita'] = element['quantita']
                data.listaProdottiMagazzino.append(new_item)

            for prodottoF in data.listaProdottiFornitore:
                if element['codice'] == prodottoF['codice']:
                    prodottoF['quantita'] -= element['quantita']
                    if prodottoF['quantita'] <= 0:
                        data.listaProdottiFornitore.remove(prodottoF)
                    break

        total = sum(prodotto['prezzo'] * prodotto['quantita'] for prodotto in self.prodSelezionati)
        messagebox.showinfo("Spesa totale", "Il totale è {:.2f}€".format(total))

        self.returnToHome()
        self.aggiornaArchivio(str(total))
        data.uploadMagazzino()
        data.uploadFornitore()
        self.popolaListaProdotti()

    # metodo che aggiorna l'archivio una volta chiuso l'ordine
    def aggiornaArchivio(self, tmp):
        data.downloadArchivioOrdini()
        codice_ordine = self.generaCodice()
        if codice_ordine != 0:
            today = date.today()
            ordine = {
                "codice": codice_ordine,
                "fornitore": "Abros",
                "totale": tmp,
                "data": today.isoformat()  # Formato stringa della data
            }
            data.archivioOrdini.append(ordine)
            data.uploadArchivioOrdini()
        else:
            self.aggiornaArchivio(tmp)

    # metodo che genera il codice da asssegnare all'ordine concluso
    def generaCodice(self):
        codice = randint(1, 1000000)
        codici_esistenti = {ordine['codice'] for ordine in data.archivioOrdini}
        while codice in codici_esistenti:
            codice = randint(1, 1000000)
        return codice
