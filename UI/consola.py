from Service.LocalitateService import LocalitateService
from Service.RutaService import RutaService


class Console:
    def __init__(self, localitate_service: LocalitateService, ruta_service: RutaService):
        self.__localitate_service = localitate_service
        self.__ruta_service = ruta_service

    def print_menu(self):
        print("1. Adaugare locatie")
        print("2. Adaugare ruta autocar")
        print("3. Afisare localitati ordonate crescator dupa nr. de rute dus-intors din care pornesc + acest nr.")
        print("4. Afisare rute care se opresc intr-un municipiu")
        print("5. Export JSON")
        print("a1. Afisare localitati")
        print("a2. Afisare rute autocar")
        print("x. Iesire")

    def run_menu(self):
        while True:
            self.print_menu()
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.ui_adaugare_localitate()
            elif optiune == '2':
                self.ui_adaugare_ruta()
            elif optiune == '3':
                self.ui_afisare_localitati_dupa_nr_rute()
            elif optiune == '4':
                self.ui_afisare_rute_care_se_opresc_in_municipiu()
            elif optiune == '5':
                self.ui_export_JSON()
            elif optiune == "a1":
                self.ui_print_localitati()
            elif optiune == "a2":
                self.ui_print_rute()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati!")

    def ui_adaugare_localitate(self):
        try:
            id_localitate = input("Dati id-ul localitatii")
            nume = input ("Dati numele localitatii")
            tip = input("Dati tipul localitatii (sat, oras, municipiu)")

            self.__localitate_service.adauga(id_localitate, nume, tip)
        except Exception as e:
            print(e)

    def ui_print_localitati(self):
        for localitate in self.__localitate_service.get_all():
            print(localitate)

    def ui_adaugare_ruta(self):
        try:
            id_ruta = input("Dati id-ul rutei")
            id_oras_pornire = input("Dati id-ul orasului de pornire")
            id_oras_oprire = input("Dati id-ul orasului de oprire")
            pret = int(input("Dati pretul rutei"))
            dus_intors = input("Dati proprietatea ca ruta sa fie dus-intors sau nu (true, false)")

            self.__ruta_service.adauga(id_ruta, id_oras_pornire, id_oras_oprire, pret, dus_intors)
        except Exception as e:
            print(e)

    def ui_print_rute(self):
        for ruta in self.__ruta_service.get_all():
            print(ruta)

    def ui_afisare_localitati_dupa_nr_rute(self):
        result = self.__ruta_service.localitati_oradonate_crescator_dupa_nr_rute_dus_intors()
        for localitate in result:
            print(f"Localitatea {localitate[0]} are {localitate[1]} rute dus-intors care pornesc de-acolo")

    def ui_afisare_rute_care_se_opresc_in_municipiu(self):
        result = self.__ruta_service.rute_care_se_opresc_in_municipiu()
        for ruta in result:
            print(f"Ruta {ruta[0]} se opreste in municipiul {ruta[1]}")

    def ui_export_JSON(self):
        filename = input("Dati numele fisierului JSON")
        self.__ruta_service.export_orase_interconectate(filename)