from datetime import date
from random import randint
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneErboristeria.GestioneSistema.gestione import Gestore
from GestioneErboristeria.GestioneSistema.data import data

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()


class Ui_Cassa(object):
    prodSelezionati = []
    totale = []

    def setupUi(self, Cassa):
        self.Frame = Cassa
        Cassa.setObjectName("Cassa")
        Cassa.resize(939, 615)
        self.label_4 = QtWidgets.QLabel(Cassa)
        self.label_4.setGeometry(QtCore.QRect(470, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tableWidgetcarrello = QtWidgets.QTableWidget(Cassa)
        self.tableWidgetcarrello.setGeometry(QtCore.QRect(20, 330, 421, 241))
        self.tableWidgetcarrello.setObjectName("tableWidgetcarrello")
        self.tableWidgetcarrello.setColumnCount(0)
        self.tableWidgetcarrello.setRowCount(0)
        self.ricercabtn = QtWidgets.QPushButton(Cassa)
        self.ricercabtn.setGeometry(QtCore.QRect(70, 30, 91, 41))
        self.ricercabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercabtn.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.ricercabtn.setIcon(icon)
        self.ricercabtn.setObjectName("ricercabtn")
        self.homebtn = QtWidgets.QPushButton(Cassa)
        self.homebtn.setGeometry(QtCore.QRect(610, 530, 111, 41))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.tableWidgetlist = QtWidgets.QTableWidget(Cassa)
        self.tableWidgetlist.setGeometry(QtCore.QRect(480, 40, 421, 241))
        self.tableWidgetlist.setObjectName("tableWidgetlist")
        self.tableWidgetlist.setColumnCount(0)
        self.tableWidgetlist.setRowCount(0)
        self.carrellobtn = QtWidgets.QPushButton(Cassa)
        self.carrellobtn.setGeometry(QtCore.QRect(150, 190, 131, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon2)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.label = QtWidgets.QLabel(Cassa)
        self.label.setGeometry(QtCore.QRect(90, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.codicele = QtWidgets.QLineEdit(Cassa)
        self.codicele.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.codicele.setObjectName("codicele")
        self.ricercale = QtWidgets.QLineEdit(Cassa)
        self.ricercale.setGeometry(QtCore.QRect(170, 40, 131, 20))
        self.ricercale.setObjectName("ricercale")
        self.quantitaprodsb = QtWidgets.QSpinBox(Cassa)
        self.quantitaprodsb.setGeometry(QtCore.QRect(260, 150, 42, 22))
        self.quantitaprodsb.setObjectName("quantitaprodsb")
        self.acquistabtn = QtWidgets.QPushButton(Cassa)
        self.acquistabtn.setGeometry(QtCore.QRect(450, 530, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon3)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.label_3 = QtWidgets.QLabel(Cassa)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Cassa)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 1200))
        self.frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(190, 220, 190, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4.raise_()
        self.tableWidgetcarrello.raise_()
        self.ricercabtn.raise_()
        self.homebtn.raise_()
        self.tableWidgetlist.raise_()
        self.carrellobtn.raise_()
        self.label.raise_()
        self.codicele.raise_()
        self.ricercale.raise_()
        self.quantitaprodsb.raise_()
        self.acquistabtn.raise_()
        self.label_3.raise_()

        self.prodSelezionati.clear
        self.totale.clear()
        self.creaListaVendita()
        self.popolaListaVendita()

        self.ricercabtn.clicked.connect(self.ricercaArticolo)
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        self.acquistabtn.clicked.connect(self.chiudiVendita)
        self.homebtn.clicked.connect(self.returnToHome)

        self.retranslateUi(Cassa)
        QtCore.QMetaObject.connectSlotsByName(Cassa)

    def retranslateUi(self, Cassa):
        _translate = QtCore.QCoreApplication.translate
        Cassa.setWindowTitle(_translate("Cassa", "Form"))
        self.label_4.setText(_translate("Cassa", "Lista prodotti:"))
        self.ricercabtn.setText(_translate("Cassa", "  Ricerca"))
        self.homebtn.setText(_translate("Cassa", "Home"))
        self.carrellobtn.setText(_translate("Cassa", "Metti nel carrello"))
        self.label.setText(_translate("Cassa", "Inserisci codice e quantità da comprare"))
        self.acquistabtn.setText(_translate("Cassa", "  Acquista"))
        self.label_3.setText(_translate("Cassa", "Carrello:"))

    # metodo che consente di tornare alla schermata di home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    # metodo crea una tabella con numero di righe variabile in base al numero di prodotti differenti presenti in magazzino
    def creaListaVendita(self):
        data.downloadMagazzino()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(5)
        self.tableWidgetlist.setRowCount(data.nFitoMagaz + data.nProdMagaz)
        for i in range(0, 5):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        item.setText(_translate("cassa", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("cassa", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("cassa", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("cassa", "Codice"))

        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    # metodo che consente di riempire la tabella andando a leggere le due liste
    # contenti rispettivamente prodotti fitoterapici e prodotti semplici presenti in magazzino
    def popolaListaVendita(self):
        _translate = QtCore.QCoreApplication.translate
        row = 0
        for prodotto in data.listaFitoMagazzino + data.listaProdottiMagazzino:
            for colonna in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(row, colonna, item)
                if colonna == 0:
                    item.setText(_translate("cassa", prodotto['nome']))
                elif colonna == 1:
                    item.setText(_translate("cassa", str(prodotto['quantita'])))
                elif colonna == 2:
                    item.setText(_translate("cassa", str(prodotto['prezzo'])))
                elif colonna == 3:
                    item.setText(_translate("cassa", str(prodotto['codice'])))
            row += 1

    # metodo che permette di ricercare tutti i prodotti disponibili all'acquisto
    def ricercaArticolo(self):
        param = self.ricercale.text()
        if param == "":
            self.popolaListaVendita()
            return
        else:
            prodottiRicercati = []
            for prodotto in data.listaFitoMagazzino:
                if param.lower() in prodotto['nome'].lower() or param in str(prodotto['codice']):
                    prodottiRicercati.append(prodotto)
            for prodotto in data.listaProdottiMagazzino:
                if param.lower() in prodotto['nome'].lower() or param in str(prodotto['codice']):
                    prodottiRicercati.append(prodotto)

            self.popolaRicerca(prodottiRicercati)

    # metodo che riempie la tabella dei prodotti in base alla ricerca effettuata
    def popolaRicerca(self, prodRicercati):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidgetlist.clear()
        self.creaListaVendita()
        row = 0
        for prodotto in prodRicercati:
            for colonna in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(row, colonna, item)
                if colonna == 0:
                    item.setText(_translate("cassa", prodotto['nome']))
                elif colonna == 1:
                    item.setText(_translate("cassa", str(prodotto['quantita'])))
                elif colonna == 2:
                    item.setText(_translate("cassa", str(prodotto['prezzo'])))
                elif colonna == 3:
                    item.setText(_translate("cassa", str(prodotto['codice'])))
            row += 1

    # metodo che gestisce la selezione di un prodotto dal magazzino e la sua aggiunta al carrello, la selezione
    # della quantità da acquistare e l'eventuale rimozione
    def selezionaProdotto(self):
        from tkinter import messagebox
        param = self.codicele.text()
        if self.quantitaprodsb.value() == 0:
            messagebox.showinfo("Errore", "Inserisci la quantità da aquistare")
            return
        listaTotale = data.listaFitoMagazzino + data.listaProdottiMagazzino
        for element in listaTotale:
            if param == element['codice']:
                if self.quantitaprodsb.value() <= element['quantita']:
                    element_selezionato = element.copy()
                    element_selezionato['quantita'] = self.quantitaprodsb.value()
                    for prodotto in self.prodSelezionati:
                        if prodotto['codice'] == param:
                            self.prodSelezionati.remove(prodotto)
                            messagebox.showinfo("Errore",
                                                "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                                                " a favore dell'inserimento del prodotto appena selezionato")
                            break

                    self.prodSelezionati.append(element_selezionato)
                    self.creaCarrello()
                    self.popolaCarrello(len(self.prodSelezionati) - 1)
                    return
                else:
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                    return

        messagebox.showinfo("Errore", "Inserisci il codice corretto")
        return

    #  metodo crea una tabella per i prodotti da acquistare
    def creaCarrello(self):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidgetcarrello.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetcarrello.setObjectName("tableWidget")
        self.tableWidgetcarrello.setColumnCount(4)
        self.tableWidgetcarrello.setRowCount(len(self.prodSelezionati))
        intestazioni = ["Prodotto", "Quantità", "Prezzo", "Codice"]
        for indice, intestazione in enumerate(intestazioni):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setHorizontalHeaderItem(indice, item)
            item.setText(_translate("cassa", intestazione))
        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    # metodo che gestisce il riempimento della tabella relativa al carrello
    def popolaCarrello(self, nProdSelezionati):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(nProdSelezionati, colonna, item)
            prodotto = self.prodSelezionati[nProdSelezionati]
            if colonna == 0:
                item.setText(_translate("cassa", prodotto['nome']))
            elif colonna == 1:
                item.setText(_translate("cassa", str(self.quantitaprodsb.value())))
            elif colonna == 2:
                item.setText(_translate("cassa", str(prodotto['prezzo'])))
            elif colonna == 3:
                item.setText(_translate("cassa", prodotto['codice']))

        self.totale.append(prodotto['prezzo'] * self.quantitaprodsb.value())

    # metodo che permette di modificare il carrello in base ai prodotti
    def modificaCarrello(self, riga, elemrimosso):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(riga, colonna, item)
            prodotto = elemrimosso
            if colonna == 0:
                item.setText(_translate("cassa", prodotto['nome']))
            elif colonna == 1:
                item.setText(_translate("cassa", str(self.quantitaprodsb.value())))
            elif colonna == 2:
                item.setText(_translate("cassa", str(prodotto['prezzo'])))
            elif colonna == 3:
                item.setText(_translate("cassa", prodotto['codice']))

        self.totale[riga] = prodotto['prezzo'] * self.quantitaprodsb.value()

    # metodo che gestisce l'effettiva vendita e l'aggiornamento del magazzino
    def chiudiVendita(self):
        if not self.prodSelezionati:
            messagebox.showinfo("Errore", "Inserisci almeno un prodotto nel carrello")
            return
        data.downloadMagazzino()
        for prodottoSelezionato in self.prodSelezionati:
            codiceProdottoSelezionato = prodottoSelezionato['codice']
            quantitaSelezionata = prodottoSelezionato['quantita']

            for indice, prodottoMagazzino in enumerate(data.listaProdottiMagazzino):
                if prodottoMagazzino['codice'] == codiceProdottoSelezionato:
                    if quantitaSelezionata >= prodottoMagazzino['quantita']:
                        data.listaProdottiMagazzino.pop(indice)
                    else:
                        prodottoMagazzino['quantita'] -= quantitaSelezionata
                    break
            else:
                for indice, farmacoMagazzino in enumerate(data.listaFitoMagazzino):
                    if farmacoMagazzino['codice'] == codiceProdottoSelezionato:
                        if quantitaSelezionata >= farmacoMagazzino['quantita']:
                            data.listaFitoMagazzino.pop(indice)
                        else:
                            farmacoMagazzino['quantita'] -= quantitaSelezionata
                        break

        tmp = str(sum([prodotto['prezzo'] * prodotto['quantita'] for prodotto in self.prodSelezionati]))
        messagebox.showinfo("Spesa totale", "Il totale è " + tmp[0:5] + "€")
        self.returnToHome()
        self.aggiornaArchivio(tmp)
        data.uploadMagazzino()

        self.popolaListaVendita()

    # metodo che aggiorna l'archivio vendite
    def aggiornaArchivio(self, tmp):
        data.downloadArchivioVendite()
        codiceVendita = self.generaCodice()
        if codiceVendita == 0:
            self.aggiornaArchivio(tmp)
            return

        today = date.today()
        vendita = {
            "codice": codiceVendita,
            "totale": tmp,
            "data": today.isoformat()
        }
        data.archivioVendite.append(vendita)
        data.uploadArchivioVendite()

    # metodo che genera il codice da assegnare alla vendite effettuata nell'archivio
    def generaCodice(self):
        codice = randint(1, 1000000)
        for element in data.archivioVendite:
            if 'codice' in element and codice == element['codice']:
                return 0
        return codice
