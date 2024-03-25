import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=702, y=404)
pyautogui.write("DESENVOLVEDOR MARCOS PICCOLO")
pyautogui.press("enter")

time.sleep(1)
pyautogui.click(x=693, y=505)
pyautogui.write("123456789")
pyautogui.press("enter")

# 3 - Importar a base de dados
import pandas

# 4 - Cadastrar o primeiro produto
#código do produto

tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:

    pyautogui.click(x=699, y=293)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria do produto
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço do produto
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str( preco_unitario))
    pyautogui.press("tab")

    # Custo do produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
