from Domain.entitate import Entitate


class Localitate(Entitate):
    def __init__(self, id_localitate, nume, tip):
        super().__init__(id_localitate)
        self.__nume = nume
        self.__tip = tip

    @property
    def nume(self):
        return self.__nume

    @property
    def tip(self):
        return self.__tip

    def __str__(self):
        return f'id localitate: {self.id_entitate}, nume: {self.nume}, tip: {self.__tip}'