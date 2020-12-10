from appium.webdriver.common.mobileby import MobileBy

class resultadosLocators(object):
    """
    Esta classe contém todos os elementos definidos para o app resultados
    """
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
    BTN_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"1ºTURNO\")')
    DROP_DOWN_ELEICOES = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                     ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View"
                     "/android.view.View/android.view.View/android.view.View/android.view.View/android"
                     ".view.View/android.view.View/android.view.View/android.view.View["
                     "2]/android.view.View[2]/android.view.View[1]"))
    BTN_2_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"2º Turno\")')
    HOME_TEXTO_RECIFE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife, PE\")')
    CANDIDATO_TEXTO_MARILIA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"MARILIA ARRAES\")')
    BTN_FAVORITAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritar\")')
    FAVORITO_TEXTO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favorito\")')
    BTN_FECHAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Fechar\")')
    BTN_ESCOLHE_TURNO_TOP = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                             ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                             "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android"
                                             ".view.View/android.view.View/android.view.View/android.view.View/android.view"
                                             ".View/android.view.View/android.view.View/android.view.View/android.view"
                                             ".View[1]/android.view.View[1]/android.view.View/android.widget.Button")
    DIALOG_1_TURNO = (MobileBy.XPATH,
                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                      "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit"
                      ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android"
                      ".view.View[3]/android.view.View[2]/android.widget.RadioButton[1]")
    BTN_CONFIRMAR_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"CONFIRMAR\")')
    BTN_RESUL = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                 ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
                                 ".view.View/android.view.View/android.view.View/android.view.View/android.widget"
                                 ".TabWidget/android.view.View[1]/android.view.View")
    BTN_PESQUISAR_CANDIDATO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pesquisar candidato\")')
    BARRA_BUSCA = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                    ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View"
                                    "/android.view.View/android.view.View/android.app.Dialog/android.view.View"
                                    "/android.view.View[1]/android.view.View[2]/android.view.View["
                                    "2]/android.view.View/android.view.View/android.widget.EditText"))
    RESULTADO_PESQUISA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"DANI PORTELA\")')
    TEXTO_SELECIONE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione\")')