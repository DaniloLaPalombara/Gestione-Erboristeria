import datetime

class Cliente:

    # classe di modellazione
    def __init__(self, nome, cognome, cf, eta, email, sesso, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.eta = eta
        self.email = email
        self.sesso = sesso
        self.indirizzo = indirizzo

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_cf(self):
        return self.cf

    def get_eta(self):
        return self.eta

    def get_email(self):
        return self.email

    def get_sesso(self):
        return self.sesso

    def get_indirizzo(self):
        return self.indirizzo

    def get_schedacliente(self):
        return f"Dati Cliente\n Nome:{self.nome} Cognome:{self.cognome} Cf:{self.cf} "


class Appuntamento:
    counter = 0

    def __init__(self, cliente: Cliente, data: datetime):
        self.cliente = cliente
        self.id_app = Appuntamento.counter
        Appuntamento.counter += 1
        self.data = data
        self.isconcluso = False

    def set_isconcluso(self):
        self.isconcluso = True

    def set_idapp(self, n: int):
        self.id_app = n

    def get_idapp(self):
        return self.id_app

    def get_stato(self):
        return self.isconcluso

    def get_cliente(self):
        return self.cliente

    def get_data(self):
        return self.data

    def get_cff(self):
        return self.get_cliente().get_cf()

    def get_schedappuntamnto(self):
        return f"Codice Appuntamento:{self.get_idapp()} cf:{self.get_cliente().get_cf()} Data:{self.data}"
