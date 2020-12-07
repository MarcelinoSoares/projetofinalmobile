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

    def realizar_busca_por_estado_e_município(self):
        """
        Este método executa o fluxo da busca por estado e municipio, no app resultados
       :retorno: tela de usuario com imformações como todos os candidatos, numeros de votos e etc
        """
        btn_escolher_local = Base.find_element(self.drive, resultadosLocators.BTN_ESCOLHER_LOCAL)
        btn_escolher_local.click()
        escolher_estado = Base.find_element(self.drive, resultadosLocators.ESCOLHER_ESTADO)
        escolher_estado.click()
        TouchAction(driver).press(x=562, y=1512).move_to(x=534, y=311).release().perform()
        escolher_PE = Base.find_element(self.drive, resultadosLocators.ESCOLHER_PE)
        escolher_PE.click()
        btn_confimar = Base.find_element(self.drive, resultadosLocators.BTN_CONFIRMAR)
        btn_confimar.click()
        escolher_municipio = Base.find_element(self.drive, resultadosLocators.ESCOLHER_MUNICIPIO)
        escolher_municipio.click()
        escolher_RECIFE = Base.find_element(self.drive, resultadosLocators.ESCOLHER_RECIFE)
        escolher_RECIFE.click()
        btn_confimar = Base.find_element(self.drive, resultadosLocators.BTN_CONFIRMAR)
        btn_confimar.click()
        btn_confimar = Base.find_element(self.drive, resultadosLocators.BTN_CONFIRMAR)
        btn_confimar.click()
        time.sleep(20)



    def realizar_fluxo_navega_menu(self):
        """
         Este método executa o fluxo de navegação no menu inferior, no app resultados
         :retorno: cada tela de categoria
        """
        btn_resultados = Base.find_element(self.drive, resultadosLocators.BTN_RESULTADOS)
        btn_resultados.click()
        btn_totalizacao = Base.find_element(self.drive, resultadosLocators.BTN_TOTALIZACAO)
        btn_totalizacao.click()
        btn_favoritos = Base.find_element(self.drive, resultadosLocators.BTN_FAVORITOS)
        btn_favoritos.click()
        btn_info = Base.find_element(self.drive, resultadosLocators.BTN_INFO)
        btn_info.click()
        time.sleep(15)