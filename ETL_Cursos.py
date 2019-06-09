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


#dotenv.load_dotenv()

#usuario = os.getenv('USUARIO_CAGR')
#senha = os.getenv('SENHA_CAGR')

Chrome = webdriver.Chrome('drivers/chromedriver')
url = 'https://cagr.sistemas.ufsc.br/arvore.xhtml?treeid=30#'
Chrome.get(url)

print("Hello World")