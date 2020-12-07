from pageObjects import Base
from pageObjects.locators import resultadosLocators
from selenium.common.exceptions import NoSuchElementException

class Home(Base):

    def is_is_home_screen(self):
        """
         Este método executa o caminho para alcançar nos testes do app resultados
        :retorno: true ou false
        """
        resultados = Base.find_element(self.drive, ResultadosLocators.BTN_RESULTADOS)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True