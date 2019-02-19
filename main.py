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

botao_cadastro_turma = Chrome.find_element_by_css_selector('#aluno9-10-10')
botao_cadastro_turma.click()

