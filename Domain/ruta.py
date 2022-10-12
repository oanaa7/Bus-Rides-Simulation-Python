from Domain.entitate import Entitate


class Ruta(Entitate):
    def __init__(self,id_ruta, id_oras_pornire, id_oras_oprire, pret, dus_intors):
        super().__init__(id_ruta)
        self.__id_oras_pornire = id_oras_pornire
        self.__id_oras_oprire = id_oras_oprire
        self.__pret = pret
        self.__dus_intors = dus_intors

    @property
    def id_oras_pornire(self):
        return self.__id_oras_pornire

    @property
    def id_oras_oprire(self):
        return self.__id_oras_oprire

    @property
    def pret(self):
        return self.__pret
    @property
    def dus_intors(self):
        return self.__dus_intors

    def __str__(self):
        return f'id ruta: {self.id_entitate}, id oras pornire: {self.__id_oras_pornire}, id oras oprire: {self.id_oras_oprire} '\
            f'pret: {self.pret}, dus-intors: {self.dus_intors}'