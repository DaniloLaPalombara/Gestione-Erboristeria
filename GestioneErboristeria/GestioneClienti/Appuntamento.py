class Appuntamento:

    # classe di modellazione
    def __init__(self, data, cliente, ora):
        self.data = data
        self.cliente = cliente
        self.ora = ora
        self.concluso = False

    def set_concluso(self, stato: bool):
        self.concluso = stato

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente

    def getOra(self):
        return self.ora

    def setOra(self, ora):
        self.ora = ora
