import pytest
from pageObjects.Welcome import Initial


@pytest.mark.usefixtures("test_setup")
class testResultados(object):

    def test_fluxo_inicial(self, test_setup):
        initial= Initial(test_setup)
        initial.realizar_fluxo_inicial()

    def test_buscar_por_estado_e_municipio(self, test_setup):
        initial= Initial(test_setup)
        initial.realizar_busca_por_estado_e_município()

    def test_buscar_menu(self, test_setup):
        initial= Initial(test_setup)
        initial.realizar_fluxo_navega_menu()
