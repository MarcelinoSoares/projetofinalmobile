import pytest
from pageObjects.Welcome import Initial


@pytest.mark.usefixtures("test_setup")
class testResultados(object):

    def test_fluxo_inicial(self, test_setup):
        """
       Este método executa o teste do fluxo no bem vindo, no app resultados
      :p aram test_setup: Conexão entre dispositivo em teste (emulado) e Appium
      :retorno: passe
       """
        initial= Initial(test_setup)
        initial.realizar_fluxo_inicial()

    def test_buscar_por_estado_e_municipio(self, test_setup):
        """
       Este método executa o teste do fluxo da busca por estado e municipio, no app resultados
       :p aram test_setup: Conexão entre dispositivo em teste (emulado) e Appium
       :retorno: fail pois já terminam as eleições
        """
        initial= Initial(test_setup)
        initial.realizar_busca_por_estado_e_município()

    def test_buscar_menu(self, test_setup):
        """
       Este método executa o teste do fluxo de navegação no menu inferior, no app resultados
       :p aram test_setup: Conexão entre dispositivo em teste (emulado) e Appium
       :retorno: passe
        """
        initial= Initial(test_setup)
        initial.realizar_fluxo_navega_menu()
