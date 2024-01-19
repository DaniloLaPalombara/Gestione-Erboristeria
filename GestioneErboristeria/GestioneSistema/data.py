import json
from datetime import datetime

from GestioneErboristeria.GestioneSistema.gestione import Gestore

gestore = Gestore()

class data:

    # Inizializziamo le collection di dati per contenere tutti i dati proveniente dai file
    listaAppuntamenti = []
    listaFitoMagazzino = []
    listaProdottiMagazzino = []
    listaProdottiFornitore = []
    listaFitoFornitore = []
    archivioClienti = []
    archivioOrdini = []
    archivioVendite = []
    nVendite = 0
    nOrdini = 0
    nClienti = 0
    nProdMagaz = 0
    nFitoMagaz = 0
    nProdForn = 0
    nFitoForn = 0

    def __init__(self):
        pass

    today = datetime.now()

    # lettura e scrittura dei file utilizzati
    @staticmethod
    def uploadArchivioVendite():
        with open(gestore.returnPth() + "GestioneErboristeria/archivioVendite.json", "w") as f:
            json.dump(data.archivioVendite, f, indent=4)

    @staticmethod
    def downloadArchivioVendite():
        with open(gestore.returnPth() + "GestioneErboristeria/archivioVendite.json", "r") as f:
            data.archivioVendite = json.load(f)
        data.nVendite = len(data.archivioVendite)

    @staticmethod
    def uploadArchivioOrdini():
        with open(gestore.returnPth() + "GestioneErboristeria/Ordine.json", "w") as f:
            json.dump(data.archivioOrdini, f, indent=4)

    @staticmethod
    def downloadArchivioOrdini():
        with open(gestore.returnPth() + "GestioneErboristeria/Ordine.json", "r") as f:
            data.archivioOrdini = json.load(f)
        data.nOrdini = len(data.archivioOrdini)

    @staticmethod
    def downloadMagazzino():
        data.downloadFitoterapiciMagazzino()
        data.downloadProdottiMagazzino()
        data.nProdMagaz = len(data.listaProdottiMagazzino)
        data.nFitoMagaz = len(data.listaFitoMagazzino)

    @staticmethod
    def downloadFornitore():
        data.downloadFitoterapiciFornitore()
        data.downloadProdottiFornitore()
        data.nProdForn = len(data.listaProdottiFornitore)
        data.nFitoForn = len(data.listaFitoFornitore)

    @staticmethod
    def uploadFornitore():
        data.uploadFitoterapiciFornitore()
        data.uploadProdottiFornitore()

    @staticmethod
    def uploadMagazzino():
        data.uploadFitoMagazzino()
        data.uploadProdottiMagazzino()

    @staticmethod
    def uploadFitoterapiciFornitore():
        with open(gestore.returnPth() + "GestioneErboristeria/fitoFornitore.json", "w") as f:
            json.dump(data.listaFitoFornitore, f, indent=4)

    @staticmethod
    def uploadProdottiFornitore():
        with open(gestore.returnPth() + "GestioneErboristeria/prodottiFornitore.json", "w") as f:
            json.dump(data.listaProdottiFornitore, f, indent=4)

    @staticmethod
    def uploadFitoMagazzino():
        with open(gestore.returnPth() + "GestioneErboristeria/fitoMagazzino.json", "w") as f:
            json.dump(data.listaFitoMagazzino, f, indent=4)

    @staticmethod
    def uploadProdottiMagazzino():
        with open(gestore.returnPth() + "GestioneErboristeria/prodottiMagazzino.json", "w") as f:
            json.dump(data.listaProdottiMagazzino, f, indent=4)

    @staticmethod
    def uploadAppuntamenti():
        with open(gestore.returnPth() + "GestioneErboristeria/appuntamenti.json", "w") as f:
            json.dump(data.listaAppuntamenti, f, indent=4)

    @staticmethod
    def downloadFitoterapiciMagazzino():
        with open(gestore.returnPth() + "GestioneErboristeria/fitoMagazzino.json", "r") as f:
            fitoterapici = json.load(f)

        data.listaFitoMagazzino.clear()
        data.listaFitoMagazzino.extend(fitoterapici)

    @staticmethod
    def downloadFitoterapiciFornitore():
        with open(gestore.returnPth() + "GestioneErboristeria/fitoFornitore.json", "r") as f:
            fiterapici = json.load(f)

        data.listaFitoFornitore.clear()
        data.listaFitoFornitore.extend(fiterapici)

    @staticmethod
    def downloadProdottiFornitore():
        with open(gestore.returnPth() + "GestioneErboristeria/prodottiFornitore.json", "r") as f:
            prodotti = json.load(f)

        data.listaProdottiFornitore.clear()
        data.listaProdottiFornitore.extend(prodotti)

    @staticmethod
    def downloadProdottiMagazzino():
        with open(gestore.returnPth() + "GestioneErboristeria/prodottiMagazzino.json", "r") as f:
            prodotti = json.load(f)

        data.listaProdottiMagazzino.clear()
        data.listaProdottiMagazzino.extend(prodotti)

    @staticmethod
    def showMagazzino():
        for prodotto in data.listaProdottiMagazzino:
            print(
                f"{prodotto.get('codice', '')} {prodotto.get('nome', '')} {prodotto.get('tipologia', '')} {prodotto.get('prezzo', '')}")
            if prodotto.get('dosaggio') is not None:
                print(prodotto['dosaggio'])
            if prodotto.get('scadenza') is not None:
                print(prodotto['scadenza'])
            print(prodotto.get('giacenza', ''))

    @staticmethod
    def downloadAppuntamenti():
        with open(gestore.returnPth() + "GestioneErboristeria/appuntamenti.json", "r") as f:
            appuntamenti = json.load(f)
        data.listaAppuntamenti.clear()
        data.listaAppuntamenti.extend(appuntamenti)

    @staticmethod
    def downloadAppuntamenti():
        with open(gestore.returnPth() + "GestioneErboristeria/appuntamenti.json", "r") as f:
            # Carica direttamente i dati dal file JSON
            data.listaAppuntamenti = json.load(f)

    @staticmethod
    def uploadAppuntamenti():
        with open(gestore.returnPth() + "GestioneErboristeria/appuntamenti.json", "w") as f:
            # Salva direttamente i dati in formato JSON
            json.dump(data.listaAppuntamenti, f, indent=4)

    @staticmethod
    def downloadArchivioClienti():
        with open(gestore.returnPth() + "GestioneErboristeria/archivioClienti.json", "r") as f:
            data.archivioClienti = json.load(f)
        data.nClienti = len(data.archivioClienti)

    @staticmethod
    def uploadArchivioClienti():
        with open(gestore.returnPth() + "GestioneErboristeria/archivioClienti.json", "w") as f:
            json.dump(data.archivioClienti, f, indent=4)
