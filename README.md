# projetofinalmobile

**Projeto de automação para o aplicativo Resultados (funcionalidades)**

Este projeto tem como objetivo automatizar alguns fluxos do apk resultados. 

Realizado por:

Alan Garcia, Danilo Ferreira, Ewertton Oliveira e Marcelino Soares.
___

**Estrutura do projeto:**

Estou usando a estrutura do Pytest para este projeto. Então, aqui está uma visão geral do meu projeto:

```
resultados/
  objetos de páginas/
      localizadores /
          resultadoslocators.py
      base.py
      paginaPrincipal.py
      resultados.py
  recursos/
      apk/
          Apk.File
  testes /
      test_Resultados.py
```

🗂 **Breve explicação para cada pasta:**

Objetos de páginas >> PageObjects relacionados, um arquivo .py para cada pasta e suas funcionalidades.

Recursos >> Aqui indicamos os apks a serem usados e também o número de série do dispositivo em teste na raiz do projeto (conftest.py).

Testes >> Fluxo de teste para a execução.
___

**Recursos**

🎯 Estou usando aqui:

Python <br>
Pytest <br>
Appium-Python-Client <br>
Selênium <br>
(e alguns complementos) <br>

🛠 Como instalar?

Basta executar o arquivo requirements.txt usando o seguinte comando no caminho raiz:

```
pip install -r requirements.txt
```
___

💻 **Configuração do ambiente de teste**

A pasta do aplicativo e o número de série do produto Android estão registrados na raiz do projeto.
Basta inserir seu número de série (dispositivos adb) em conftest.py.

Depois disso, indique

Para executar o projeto, basta chamar pytest no terminal:

```
pytest
```
___

📝 **Execução de relatório**

Para realizar a execução e também gerar um relatório para isso, basta usar o seguinte comando ao chamar o pytest:

```
pytest --html = report.html
```

Após a execução, um arquivo denominado "report.html" será gerado no caminho raiz do projeto. Clique nele e ele será aberto como um arquivo de texto. Execute-o indicando um navegador para renderizar o arquivo html. O relatório será exibido.

Além disso, um link será exibido após a execução, para que você possa acessá-lo diretamente a partir dele.

___
