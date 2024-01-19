from GestioneErboristeria.GestioneVendite.Prodotto import Prodotto


class Fitoterapico(Prodotto):

    # classe di modellazione
    def __init__(self, codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza):
        super().__init__(codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza)
