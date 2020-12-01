from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
Este método é responsável por encontrar elementos (com presence_of_element_located condição)
:p ou elemento: elemento a ser pesquisado
:retorno: valor do elemento
 """

class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def find_element(self, element):
        wait = WebDriverWait(self, 20)
        value = wait.until(EC.presence_of_element_located((
            element
        )))
        return value
