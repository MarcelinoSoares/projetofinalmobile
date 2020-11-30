from appium.webdriver.common.mobileby import MobileBy


class resultadosLocators(object):
    BTN_PROX = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Próximo\")')
    BTN_ENTENDI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Entendi\")')
    BTN_LI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Li e Aceito\")')
    BTN_PERMITIR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Permitir\")')
    BTN_RESULTADOS = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Resultados\")')
    BTN_TOTALIZACAO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Totalização\")')
    BTN_FAVORITOS = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritos\")')
    BTN_INFO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Informações\")')
    BTN_ESCOLHER_LOCAL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Escolher local\")')
    BTN_PESQUISAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pesquisar candidato\")')
    ESCOLHER_ESTADO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Estado Selecione o estado\")')
    ESCOLHER_MUNICIPIO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Município Selecione o município\")')
    ESCOLHER_PE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pernambuco\")')
    ESCOLHER_RECIFE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife\")')
    BTN_CONFIRMAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Confirmar\")')
