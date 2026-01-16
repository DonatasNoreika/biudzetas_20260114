import pickle
from models import PajamuIrasas, IslaiduIrasas


class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.zurnalas = self.nuskaityti_is_failo()

    def nuskaityti_is_failo(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except FileNotFoundError:
            zurnalas = []
        return zurnalas

    def irasyti_i_faila(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def isimti(self, suma, isigyta, info):
        irasas = IslaiduIrasas(suma, isigyta, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def parodyti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas:", suma)
