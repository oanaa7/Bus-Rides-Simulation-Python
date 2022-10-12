from Domain.localitate_validator import LocalitateValidator
from Domain.ruta_validator import RutaValidator
from Repository.file_repository import FileRepository
from Service.LocalitateService import LocalitateService
from Service.RutaService import RutaService
from Tests.run_all import run_all_tests
from UI.consola import Console


def main():
    #run_all_tests()

    localitati_repository = FileRepository("localitati.txt")
    localitate_validator = LocalitateValidator()
    rute_repository = FileRepository("rute.txt")
    ruta_validator = RutaValidator()

    localitate_service = LocalitateService(localitati_repository, localitate_validator)
    ruta_service =RutaService(rute_repository, ruta_validator, localitati_repository)

    consola = Console(localitate_service, ruta_service)
    consola.run_menu()

main()