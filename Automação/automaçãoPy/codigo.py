# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar dois botões ao mesmo tempo
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5  #da uma pausa de 0,5 segundos em toda ação que acontece no site


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
#pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write("file:///C:/Users/Luzineia/OneDrive/Documentos/PythonHash/tabela/index.html")
pyautogui.press("enter")

time.sleep(3) # Da uma pausa apenas nessa ação
#pyautogui.click(x=774,y=364)
pyautogui.press("tab")
pyautogui.write("Otavio Vinicius")
pyautogui.press("tab")
pyautogui.write("vinicitu@gmail.com")
pyautogui.press("tab")
pyautogui.write("11 982050837")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

tabela = pd.read_csv("produtos.csv")
print(tabela)

pyautogui.press("tab")


for linha in tabela.index:
    pyautogui.PAUSE = 1.0
    #pyautogui.click(x=799, y=246)
    #código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria do produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preco Unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #Custo de produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    #eviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    #pyautogui.click(x= 873, y= 905)
    pyautogui.scroll(5000)
