from appium.webdriver.common.mobileby import MobileBy


class resultadosLocators(object):
    BTN_PROX = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Próximo\")')
    BTN_ENTENDI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Entendi\")')
    BTN_LI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Li e Aceito\")')
    BTN_PERMITIR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Permitir\")')
    BTN_RESULTADOS = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Resultos\")')