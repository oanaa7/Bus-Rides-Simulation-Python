from Domain.localitate import Localitate
from Domain.localitate_validator import LocalitateValidator
from Repository.file_repository import FileRepository
from Service.LocalitateService import LocalitateService
from Tests.utils import clear_file


def test_adauga_localitate():
    clear_file("localitati-test.txt")
    localitati_repository = FileRepository("localitati-test.txt")
    localitate_validator = LocalitateValidator()

    localitate_service = LocalitateService(localitati_repository, localitate_validator)

    localitate_service.adauga('1', "Fagaras", "municipiu")
    assert len(localitate_service.get_all()) == 1
    added = localitati_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == "Fagaras"
    assert added.tip == "municipiu"

    try:
        localitate_service.adauga('1', "Brasov", "oras")
        assert False
    except Exception:
        assert True