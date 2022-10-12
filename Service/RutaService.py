import json

from Domain.ruta import Ruta
from Domain.ruta_validator import RutaValidator
from Repository.file_repository import FileRepository


class RutaService:
    def __init__(self, rute_repository: FileRepository, ruta_validator: RutaValidator, localitati_repository: FileRepository):
        self.__rute_repository = rute_repository
        self.__ruta_validator = ruta_validator
        self.__localitati_repository = localitati_repository

    def adauga(self, id_ruta, id_oras_pornire, id_oras_oprire, pret, dus_intors):
        '''
        adauga o ruta
        :param id_ruta: id-ul rutei - string
        :param id_oras_pornire: id-ul orasului de pronire - string
        :param id_oras_oprire: id-ul orasului d eoprire - string
        :param pret: pretul rutei - numar intreg
        :param dus_intors: string ("true" sau "false")
        :return:
        '''
        if self.__localitati_repository.find_by_id(id_oras_pornire) is None:
            raise KeyError("Nu exista un oras cu id-ul de pornire")
        if self.__localitati_repository.find_by_id(id_oras_oprire) is None:
            raise KeyError("Nu exista un oras cu id-ul de oprire")

        ruta = Ruta(id_ruta, id_oras_pornire, id_oras_oprire, pret, dus_intors)
        self.__ruta_validator.validate(ruta)

        self.__rute_repository.adauga(ruta)

    def get_all(self):
        '''

        :return: lista de rute
        '''
        return self.__rute_repository.get_all()

    def localitati_oradonate_crescator_dupa_nr_rute_dus_intors(self):
        '''
        localitățile ordonate crescător după numărul de rute dus-întors care pornesc din ele + numarul
        :return: o lista de tupluri continand orasele ordonate crescator
        dupa nr. de rute dus-intors din care pornesc + acest nr.
        '''

        result = {}  # dict cu keys: localitati
        for localitate in self.__localitati_repository.get_all():
            result[localitate.id_entitate] = 0

        for ruta in self.get_all():
            if ruta.dus_intors == 'true':
                result[ruta.id_oras_pornire] += 1

        result2 = sorted(result.items(), key=lambda x: x[1])
        lista = []
        for elem in result2:
            localitate = self.__localitati_repository.find_by_id(elem[0])
            lista.append((localitate, elem[1]))
        return lista

    def rute_care_se_opresc_in_municipiu(self):
        '''
        Rutele care se opresc într-o localitate minicipiu. Se vor afișa și denumirile localităților
        :return: o lista de tupluri continand rutele care se opresc in municipii, impreuna cu numele acelor localitati
        '''
        result = []
        for ruta in self.get_all():
            localitate_oprire = self.__localitati_repository.find_by_id(ruta.id_oras_oprire)
            if localitate_oprire.tip == 'municipiu':
                result.append((ruta, localitate_oprire.nume))
        return result

    def export_orase_interconectate(self):
        '''
        scrie intr-un fisier JSON orasele interconectate
        localitățile cu o listă cu numele localităților în care ajunge cel puțin o rută care pornește din localit.
        :param filename: numele fisieurlui in care se va face exportul - string
        :return:
        '''
        result = {}  # dict cu keys: localitate_pornire si values: localitate_oprire

        for ruta in self.get_all():
            pornire = self.__localitati_repository.find_by_id(ruta.id_oras_pornire).nume
            oprire = self.__localitati_repository.find_by_id(ruta.id_oras_oprire).nume
            if pornire in result:
                if oprire not in result[pornire]:
                    result[pornire].append(oprire)
            else:
                result[pornire] = [oprire]

        with open('export.json', 'w') as f:
            json.dump(result, f, indent=2)







