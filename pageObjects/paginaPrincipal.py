from pageObjects import Base
from pageObjects.locators.resultadosLocators import *
import time

class Initial(Base):

    def realizar_fluxo_inicial(self):
        """
       Este método executa o fluxo no bem vindo, no app resultados
       :retorno: tela de usuario
        """
        btn_prox = Base.find_element(self.drive, resultadosLocators.BTN_PROX)
        btn_prox.click()
        btn_entendi = Base.find_element(self.drive, resultadosLocators.BTN_ENTENDI)
        btn_entendi.click()
        TouchAction(self.drive).press(x=487, y=1538).move_to(x=497, y=515).release().perform()
        btn_li = Base.find_element(self.drive, resultadosLocators.BTN_LI)
        btn_li.click()
        btn_permitir = Base.find_element(self.drive, resultadosLocators.BTN_PERMITIR)
        btn_permitir.click()
        time.sleep(20)