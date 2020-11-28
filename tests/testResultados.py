import pytest
from pageObjects.Welcome import Initial


@pytest.mark.usefixtures("test_setup")
class testResultados(object):
    def test_fluxo_inicial(self, test_setup):
        initial= Initial(test_setup)
        initial.realizar_fluxo_inicial()
