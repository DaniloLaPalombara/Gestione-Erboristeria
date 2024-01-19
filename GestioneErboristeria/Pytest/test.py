import datetime
from os.path import abspath
from unittest import TestCase

from GestioneErboristeria.GestioneSistema.gestione import Gestore

gestore = Gestore()
#Classe di sviluppo di Py test
class TestVari(TestCase):

    #Metodo che testa il path assoluto del file corrente
    #path utilizzato per prendere le risorse grafiche quali immagini, loghi e sfondi
    def test_Path(self):

        abp = abspath("")
        split = [abp.split("\\")]
        pthArr = []
        finPth = ""

        for element in split:
            if element == split[len(split) - 1]:
                pthArr += element
        for x in range(len(pthArr)-1):
            finPth += str(pthArr[x]) + "/"

        stringa = gestore.returnPth()
        assert stringa == finPth


    # Test utilizzato per capire se le date
    # utilizzate sono le stesse
    def test_lettura_datetime(self):

        today2 = datetime.date.today()
        giornoo = datetime.date(2024, 1, 1)


        assert today2 == giornoo



