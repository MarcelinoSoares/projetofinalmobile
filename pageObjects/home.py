from pageObjects import Base
from pageObjects.locators import resultadosLocators
from selenium.common.exceptions import NoSuchElementException

"""
Este método executa o caminho para alcançar nos testes do app resultados
:retorno: true ou false
"""

class Home(Base):
    def is_is_home_screen(self):
        resultados = Base.find_element(self.drive, ResultadosLocators.BTN_RESULTADOS)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True