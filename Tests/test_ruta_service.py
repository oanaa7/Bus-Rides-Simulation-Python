from Domain.localitate import Localitate
from Domain.localitate_validator import LocalitateValidator
from Domain.ruta_validator import RutaValidator
from Repository.file_repository import FileRepository
from Service.LocalitateService import LocalitateService
from Service.RutaService import RutaService
from Tests.utils import clear_file


def test_ruta_service():
    clear_file("localitate-test.txt")
    clear_file("rute-test.txt")
    localitati_repository = FileRepository("localitate-test.txt")

    rute_repository = FileRepository("rute-test.txt")
    ruta_validator = RutaValidator()

    ruta_service = RutaService(rute_repository, ruta_validator, localitati_repository)

    localitati_repository.adauga(Localitate('1', "Fagaras", "municipiu"))
    localitati_repository.adauga(Localitate('2', "Brasov", "oras"))

    ruta_service.adauga('1', "1", "2", 10,"true")
    assert len(rute_repository.get_all()) == 1
    added = rute_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.id_oras_pornire == "1"
    assert added.id_oras_oprire == "2"
    assert added.pret == 10
    assert added.dus_intors == "true"

    try:
        ruta_service.adauga('2', "2", "3", 10,"true")
        assert False
    except Exception:
        assert True

    localitati_ordonate = ruta_service.localitati_oradonate_crescator_dupa_nr_rute_dus_intors()

    assert localitati_ordonate[0][0].id_entitate == "2"
    assert localitati_ordonate[0][1] == 0
    assert localitati_ordonate[1][0].id_entitate == "1"
    assert localitati_ordonate[1][1] == 1

    ruta_service.adauga('2', "2", "1", 10,"true")
    rute_in_municipiu = ruta_service.rute_care_se_opresc_in_municipiu()
    assert len(rute_in_municipiu) == 1
    assert rute_in_municipiu[0][0].id_entitate == '2'
    assert rute_in_municipiu[0][1] == "Fagaras"