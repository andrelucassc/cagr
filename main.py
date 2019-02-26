from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import logging
import pandas as pd
import dotenv
import os
import time

dotenv.load_dotenv()

usuario = os.getenv('USUARIO_CAGR')
senha = os.getenv('SENHA_CAGR')

Chrome = webdriver.Chrome('drivers/chromedriver')
url = 'https://cagr.sistemas.ufsc.br/modules/aluno/'
Chrome.get(url)

campo_username = Chrome.find_element_by_css_selector('#username')
campo_username.send_keys(usuario)

campo_password = Chrome.find_element_by_css_selector('#password')
campo_password.send_keys(senha)

botao_enter = Chrome.find_element_by_css_selector('#fm1 > div > input')
botao_enter.click()

# Caso usuário precise preencher pesquisa do CAGR, clicar para voltar para o CAGR
try:
    botao_voltar_cagr = Chrome.find_element_by_css_selector('#j_id20 > input[type="submit"]:nth-child(2)')
    botao_voltar_cagr.click()
except:
    pass

botao_cadastro_turma = Chrome.find_element_by_css_selector('#aluno9-10-10')
botao_cadastro_turma.click()


def get_data(driver):
    """Carrega os dados da tabela de cadastro de turmas."""
    
    tabela = driver.find_element_by_xpath('//*[@id="formBusca:dataTable"]')

    dfs = pd.read_html(tabela.get_attribute('outerHTML'), index_col=0)

    return dfs[0]

next_button = Chrome.find_element_by_xpath('//*[@id="formBusca:dataScroller1_table"]/tbody/tr/td[15]')

data = pd.DataFrame()

for i in range(108):

    new_data = get_data(Chrome)

    data = data.append(new_data, sort=False)

    try:
        next_button = Chrome.find_element_by_xpath('//*[@id="formBusca:dataScroller1_table"]/tbody/tr/td[15]')
        next_button.click()
        time.sleep(3)

    except:
        print('Saindo do Loop....')
        break
    

print('Antes de dropar os duplicados, forma do data frame era:')
print(data.shape)
data = data.drop_duplicates()
print('Depois de dropar:')
print(data.shape)

print(data)
print(data.size)

print(data.tail())


data.to_csv('Dados CAGR.csv', sep=';')
