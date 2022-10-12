from copy import deepcopy

import jsonpickle as jsonpickle

from Domain.entitate import Entitate


class FileRepository:
    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __read_file(self):
        '''
        citeste din fisier datele
        :return:
        '''
        try:
            with open(self.__filename, 'r') as fp:
                # return json.load(fp)
                self.__storage = jsonpickle.decode(fp.read())
        except:
            self.__storage = {}

    def __write_file(self):
        '''
        scrie in fisier datele
        :return:
        '''
        with open(self.__filename, 'w') as fp:
            # json.dump(lista, fp)
            fp.write(jsonpickle.encode(self.__storage))

    def find_by_id(self, id_entitate):
        '''
        cauta entitatea cu id-ul dat
        :param id_entitate: string
        :return: entiatea cu id-ul dat, daca aceasta exista, sau None in caz contrar
        '''
        self.__read_file()
        if id_entitate in self.__storage:
            return deepcopy(self.__storage[id_entitate])
        return None

    def get_all(self):
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def adauga(self, entitate: Entitate):
        '''
        adauga o entitate
        :param entitate: un obiect de tipul Entitate
        :return:
        '''
        if self.find_by_id(entitate.id_entitate):
            raise KeyError(f"Exista deja o masina cu id-ul {entitate.id_entitate}")
        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def delete(self, id_entitate):
        '''
        sterge o entitate dupa id
        :param id_entitate: string
        :return:
        '''
        if self.find_by_id(id_entitate) is None:
            raise KeyError(f"Nu exista masina cu id-ul {id_entitate}")
        del self.__storage[id_entitate]
        self.__write_file()

    def update(self, entitate: Entitate):
        '''
        updateaza o entitate dupa id
        :param entitate: un obiect de tipul Entitate
        :return:
        '''
        if self.find_by_id(entitate.id_entitate) is None:
            raise KeyError(f"Nu exista masina cu id-ul {entitate.id_entitate}")

        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()