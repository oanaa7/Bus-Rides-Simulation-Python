from Domain.localitate import Localitate


class LocalitateValidator:
    def validate(self, localitate: Localitate):
        erori = []
        if localitate.nume == '':
            erori.append('Numele nu poate fi gol')
        if localitate.tip not in ['sat', 'oras', 'municipiu']:
            erori.append('Tipul localitatii trebuie sa fie sat, oras sau municipiu')

        if len(erori) > 0:
            raise ValueError(erori)
