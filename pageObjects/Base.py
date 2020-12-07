from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.locators.resultadosLocators import resultadosLocators

class Base(object):

    def __init__(self, drive):
        """
         Este método é responsável por encontrar elementos (com presence_of_element_located condição)
         :p ou elemento: elemento a ser pesquisado
        :retorno: valor do elemento
        """
        self.drive = drive

    def find_element(self, element):
        value = WebDriverWait(self, 30).until(EC.presence_of_element_located((
            element
        )))
        return value

    def is_is_home_screen(self):
        resultados = Base.find_element(self.drive, resultadosLocators.EXPRESSION_SELECIONE)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True
