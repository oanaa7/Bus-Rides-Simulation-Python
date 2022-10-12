from Domain.ruta import Ruta


class RutaValidator:
    def validate(self, ruta: Ruta):
        erori = []
        if ruta.id_oras_pornire == ruta.id_oras_oprire:
            erori.append("id-ul orasului de pornire trebuie sa fie diferit de id-ul orasului de oprire")
        if ruta.dus_intors not in ["true", "false"]:
            erori.append('Campul dus-intors poate fi doar true sau false')

        if len(erori) > 0:
            raise ValueError(erori)
