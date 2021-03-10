import time                                                 #
import json                                                             #
from selenium import webdriver                                                     #
from selenium.webdriver.chrome.options import Options                                       #        
from selenium import webdriver                                                                 # IMPORTAR BIBLIOTECAS
from selenium.webdriver.common.by import By                                                 #                                       
from selenium.webdriver.common.action_chains import ActionChains                         #
from selenium.webdriver.support import expected_conditions                            #
from selenium.webdriver.support.wait import WebDriverWait                          #
from selenium.webdriver.common.keys import Keys                                 #
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities#


class ChromeAutenticao:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(         # OBTEM O DIRETÓRIO E USA O CHROMEDRIVER
            executable_path='D:/TRABALHO/Selenium-huggy/chromedriver.exe')
                
# 'C:/Users/luan.portugal/Desktop/HuggySelenium/chromedriver.exe'

    def Colocar_Flow(self): # FUNÇÃO PARA INCIAR A TROCA DO FLOW
        self.driver.get('https://www.huggy.app/?return=https%3A%2F%2Flegacy.huggy.app%2Fpanel%2F')   # ACESSA O LINK NO QUAL SE FAZ O SELENIUM
        self.driver.maximize_window()    # COLOCAR A TELA CHEIA DE ACORDO COM A RESOLUÇÃO DA TELA 
        time.sleep(2)  # ESPERA 2 SEGUNDOS ANTES DE INICIAR
        self.driver.switch_to.frame(1) # RENDERIZA 1 FRAME PARA A EXECUÇÃO


################################################## SESSÃO DE LOGIN #######################################################################################
       
        self.driver.find_element(By.ID, "input_11").click()     # CLICAR NO INPUT DE EMAIL
        self.driver.find_element(By.ID, "input_11").send_keys("leonardo.henriques@bradvisors.com.br")   # COLOCAR EMAIL NO INPUT DE EMAIL
        self.driver.find_element(By.CSS_SELECTOR, ".Button_button_3qErG:nth-child(3)").click()    # CLICAR NO INPUT DE EMAIL
        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.find_element(By.ID, "input_17").click()     # CLILCAR NO INPUT SENHA
        self.driver.find_element(By.ID, "input_17").send_keys("Bra123456") # COLOCAR A SENHA NO INPUT SENHA
        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.find_element(By.CSS_SELECTOR, ".Button_block_2cQNN").click() # CLICAR NO BOTÃO DE LOGIN E FAZER LOGIN


################################################# SESSÃO DENTRO DO HUGGY, ACESSANDO ATÉ A TROCA DO FLOW ##################################################

        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.get('https://www.huggy.app/panel/config/channels/whatsapp-business-api')
        time.sleep(2) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.CLASS_NAME, "htable-column-label").click()    # CLICAR EM WHATS VERIFICADO
        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.find_element(By.CSS_SELECTOR, ".form-item:nth-child(9) .ms-choice > span").click()    # CLICAR NO SELECIONADOR DE FLOW DE SAÍDA
        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.find_element(By.CSS_SELECTOR, ".form-item:nth-child(9) li:nth-child(1) > label").click()    # CLICAR NO FLOW: saida_JV
        time.sleep(2) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA 
        self.driver.find_element(By.CSS_SELECTOR, ".hgs-right > .btn").click()    # CLILCAR EM SALVAR
        time.sleep(3)
        self.driver.close()        # FECHA O NAVEGADOR
# FINISH
        

bot = ChromeAutenticao() # INSTANCIAR A CLASSE
bot.Colocar_Flow() # INSTANCIAR A FUNÇÃO DENTRO DA CLASSE
