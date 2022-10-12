from Domain.localitate import Localitate
from Domain.localitate_validator import LocalitateValidator
from Repository.file_repository import FileRepository


class LocalitateService:
    def __init__(self, localitati_repository: FileRepository, localitati_validator: LocalitateValidator):
        self.__localitati_repository = localitati_repository
        self.__localitate_validator = localitati_validator

    def adauga(self, id_localitate, nume, tip):
        '''
        adauga o localitate
        :param id_localitate: id-ul localitatii - string
        :param nume: numele loclaitatii - string nenul
        :param tip: tipul localitatii - string (sat, oras, municipiu)
        :return:
        '''
        localitate = Localitate(id_localitate, nume, tip)
        self.__localitate_validator.validate(localitate)
        self.__localitati_repository.adauga(localitate)

    def get_all(self):
        '''

        :return: lista de localitati
        '''
        return self.__localitati_repository.get_all()