from Tests.test_localitate_service import test_adauga_localitate
from Tests.test_repository import  test_delete_repository, \
    test_update_repository, test_add_repository
from Tests.test_ruta_service import test_ruta_service


def run_all_tests():
    test_add_repository()
    test_delete_repository()
    test_update_repository()

    test_adauga_localitate()
    test_ruta_service()