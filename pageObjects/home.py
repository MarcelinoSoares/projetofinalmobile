from pageObjects import Base
from pageObjects.locators import resultadosLocators
from selenium.common.exceptions import NoSuchElementException


class Home(Base):
    def is_is_home_screen(self):
        resultados = Base.find_element(self.drive, ResultadosLocators.BTN_RESULTADOS)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True