import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tkinter import messagebox

from GestioneErboristeria.GestioneSistema.data import data
from GestioneErboristeria.GestioneSistema.gestione import Gestore

gestore = Gestore()


class Ui_DialogCalendario(object):

    def setupUi(self, DialogCalendario):
        self.Frame = DialogCalendario
        self.ricerca = ['', "Non Concluso", "Concluso"]
        self.registrazione = QtWidgets.QFrame()

        DialogCalendario.setObjectName("DialogCalendario")
        DialogCalendario.resize(1185, 800)
        DialogCalendario.setStyleSheet("QWidget#DialogCalendario{\n"
                                       "background-color: rgb(190, 220, 190, 255);}")
        self.label = QtWidgets.QLabel(DialogCalendario)
        self.label.setGeometry(QtCore.QRect(110, 120, 971, 61))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(DialogCalendario)
        self.calendarWidget.selectionChanged.connect(self.popolaCalendario)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 210, 451, 471))
        self.calendarWidget.setObjectName("calendarWidget")
        self.nuovoappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.nuovoappbtn.clicked.connect(self.openRegistrazione)
        self.nuovoappbtn.setGeometry(QtCore.QRect(520, 470, 161, 41))
        self.nuovoappbtn.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.nuovoappbtn.setObjectName("nuovoappbtn")
        self.AppuntamentiTable = QtWidgets.QTableWidget(DialogCalendario)
        self.AppuntamentiTable.setGeometry(QtCore.QRect(520, 210, 621, 231))
        self.AppuntamentiTable.setObjectName("AppuntamentiTable")
        self.AppuntamentiTable.setColumnCount(5)
        self.AppuntamentiTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(4, item)
        self.ricercaappCombo = QtWidgets.QComboBox(DialogCalendario)
        self.ricercaappCombo.addItems(self.ricerca)
        self.ricercaappCombo.activated.connect(self.filtraAppuntamenti)
        self.ricercaappCombo.setGeometry(QtCore.QRect(530, 580, 161, 21))
        self.ricercaappCombo.setObjectName("ricercaappCombo")
        self.showdate_2 = QtWidgets.QLabel(DialogCalendario)
        self.showdate_2.setGeometry(QtCore.QRect(530, 540, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.showdate_2.setFont(font)
        self.showdate_2.setObjectName("showdate_2")
        self.chiudiappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.chiudiappbtn.clicked.connect(self.chiudiAppuntamento)
        self.chiudiappbtn.setGeometry(QtCore.QRect(720, 470, 161, 41))
        self.chiudiappbtn.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.chiudiappbtn.setObjectName("chiudiappbtn")
        self.eliminaappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.eliminaappbtn.setGeometry(QtCore.QRect(930, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.eliminaappbtn.setFont(font)
        self.eliminaappbtn.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "")
        self.eliminaappbtn.setObjectName("eliminaappbtn")
        self.homebtn = QtWidgets.QPushButton(DialogCalendario)
        self.homebtn.setGeometry(QtCore.QRect(910, 640, 151, 41))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")

        self.homebtn.clicked.connect(self.returnToHome)
        self.nuovoappbtn.clicked.connect(self.openRegistrazione)
        self.eliminaappbtn.clicked.connect(self.eliminaAppuntamento)

        self.retranslateUi(DialogCalendario)
        QtCore.QMetaObject.connectSlotsByName(DialogCalendario)

    def retranslateUi(self, DialogCalendario):
        _translate = QtCore.QCoreApplication.translate
        DialogCalendario.setWindowTitle(_translate("DialogCalendario", "Dialog"))
        self.label.setText(_translate("DialogCalendario", "CALENDARIO        APPUNTAMENTI"))
        self.nuovoappbtn.setText(_translate("DialogCalendario", "Nuovo Appuntamento"))
        item = self.AppuntamentiTable.horizontalHeaderItem(0)
        item.setText(_translate("DialogCalendario", "Codice"))
        item = self.AppuntamentiTable.horizontalHeaderItem(1)
        item.setText(_translate("DialogCalendario", "CF"))
        item = self.AppuntamentiTable.horizontalHeaderItem(2)
        item.setText(_translate("DialogCalendario", "Data"))
        item = self.AppuntamentiTable.horizontalHeaderItem(3)
        item.setText(_translate("DialogCalendario", "Stato"))
        item = self.AppuntamentiTable.horizontalHeaderItem(4)
        self.showdate_2.setText(_translate("DialogCalendario", "Ricerca per:"))
        self.chiudiappbtn.setText(_translate("DialogCalendario", "Chiudi Appuntamento"))
        self.eliminaappbtn.setText(_translate("DialogCalendario", "Elimina Appuntamento"))
        self.homebtn.setText(_translate("DialogCalendario", "Home"))

    # metodo che consente di aprire il modulo di registrazione appuntamento
    def openRegistrazione(self):
        from GestioneErboristeria.Gui.GestioneAppuntamenti.registrazione import Ui_Registrazione
        self.registrazione = QtWidgets.QFrame()
        self.ui = Ui_Registrazione()
        self.ui.setupUi(self.registrazione)
        self.registrazione.show()

    # metodo che consente di tornare alla home
    def returnToHome(self):
        from GestioneErboristeria.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che consente di prendere la data selezionata sul calendario e di trasformata in una stringa per usarla nei confronti
    def getgiorno(self):
        giorno = self.calendarWidget.selectedDate().toPyDate().strftime("%y-%m-%d")
        return giorno

    # metodo che aggiunge un nuovo appuntamento
    def aggiungiAppuntamento(self, data_appuntamento, cliente_dizionario):
        nuovo_appuntamento = {
            "id_appuntamento": self.calcolaProssimoIdAppuntamento(),
            "data": data_appuntamento,
            "cliente": cliente_dizionario,
            "concluso": False
        }

        data.listaAppuntamenti.append(nuovo_appuntamento)
        data.uploadAppuntamenti()

    # metodo che calcolo il numero dell'appuntamento successivo
    def calcolaProssimoIdAppuntamento(self):
        if not data.listaAppuntamenti:
            return 1
        else:
            return max(appuntamento['id_appuntamento'] for appuntamento in data.listaAppuntamenti) + 1

    # metodo che popola il calendario con gli appuntamenti
    def popolaCalendario(self):
        self.AppuntamentiTable.setRowCount(0)
        data.downloadAppuntamenti()
        for appuntamento in data.listaAppuntamenti:
            data_appuntamento = appuntamento['data']
            if data_appuntamento == self.getgiorno():
                row = self.AppuntamentiTable.rowCount()
                self.AppuntamentiTable.insertRow(row)
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento['id_appuntamento'])))
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento['cliente']['cf']))
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(data_appuntamento))
                stato = "Concluso" if appuntamento['is_concluso'] else "Non concluso"
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem(stato))

    # metodo che consente di visualizzare gli appuntamenti conclusi o non
    def filtraAppuntamenti(self):
        if self.ricercaappCombo.currentText() == "Non Concluso":
            self.visualizzaNonConclusi()
        elif self.ricercaappCombo.currentText() == "Concluso":
            self.visualizzaConclusi()
        elif self.ricercaappCombo.currentText() == '':
            self.AppuntamentiTable.setRowCount(0)

    # metodo che consente di visualizzare nella tabella gli appuntamenti non conclusi
    def visualizzaNonConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        data.downloadAppuntamenti()
        row = 0
        for appuntamento in data.listaAppuntamenti:
            concluso = appuntamento.get('concluso', False)
            if not concluso:
                self.AppuntamentiTable.insertRow(row)
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento['id_appuntamento'])))
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento['cliente']['cf']))
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento['data']))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                row += 1

    # metodo che consente di visualizzare nella tabella gli appuntamenti conclusi
    def visualizzaConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        data.downloadAppuntamenti()
        row = 0
        for appuntamento in data.listaAppuntamenti:
            if appuntamento['concluso']:
                self.AppuntamentiTable.insertRow(row)
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento['id_appuntamento'])))
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento['cliente']['cf']))
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento['data']))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                row += 1

    # metodo che consente di eliminare un appuntamento
    def eliminaAppuntamento(self):
        from tkinter import messagebox
        selected_row = self.AppuntamentiTable.currentRow()
        if selected_row != -1:
            id_app = int(self.AppuntamentiTable.item(selected_row, 0).text())
            data.downloadAppuntamenti()

            appuntamento_da_eliminare = next(
                (app for app in data.listaAppuntamenti if app['id_appuntamento'] == id_app),
                None
            )

            if appuntamento_da_eliminare and not appuntamento_da_eliminare.get('concluso', False):
                data.listaAppuntamenti.remove(appuntamento_da_eliminare)
                data.uploadAppuntamenti()
                messagebox.showinfo("Avviso", "Appuntamento eliminato")
            else:
                messagebox.showinfo("Avviso", "Appuntamento già concluso o non trovato!")
        else:
            messagebox.showinfo("Errore", "Seleziona una riga")

    # metodo che consente di chiudere un appuntamento
    def chiudiAppuntamento(self):
        selected_row = self.AppuntamentiTable.currentRow()
        if selected_row != -1:
            id_app = int(self.AppuntamentiTable.item(selected_row, 0).text())
            data.downloadAppuntamenti()
            appuntamento_da_concludere = next(
                (app for app in data.listaAppuntamenti if app['id_appuntamento'] == id_app),
                None)
            if appuntamento_da_concludere:
                data_app = datetime.datetime.strptime(appuntamento_da_concludere['data'], "%Y-%m-%d")
                if datetime.date.today() >= data_app.date():
                    if not appuntamento_da_concludere['concluso']:
                        appuntamento_da_concludere['concluso'] = True
                        data.uploadAppuntamenti()
                        messagebox.showinfo("Avviso", "Appuntamento concluso")
                    else:
                        messagebox.showinfo("Avviso", "Appuntamento già concluso!")
                else:
                    messagebox.showinfo("Avviso", "Non puoi concludere un appuntamento prima della sua data!")
            else:
                messagebox.showinfo("Errore", "Appuntamento non trovato")
        else:
            messagebox.showinfo("Errore", "Seleziona una riga")
