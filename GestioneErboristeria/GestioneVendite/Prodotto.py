class Prodotto():

    # classe di modellazione
    def __init__(self, codice, nome, tipologia, prezzo, dosaggio, scadenza):
        self.codice = codice
        self.nome = nome
        self.tipologia = tipologia
        self.prezzo = prezzo
        self.dosaggio = dosaggio
        self.scadenza = scadenza
        self.quantita = 0

    def getCodice(self):
        return self.codice

    def setCodice(self, codice):
        self.codice = codice

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome
