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
            executable_path='C:/Users/luan.portugal/Desktop/HuggySelenium/chromedriver.exe')
        

    def ColocarFlow(self): # FUNÇÃO PARA INCIAR COLOCAR FLOW
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
        self.driver.find_element(By.ID, "input_17").send_keys("dawdawdawdawdadawd") # COLOCAR A SENHA NO INPUT SENHA
        time.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        self.driver.find_element(By.CSS_SELECTOR, ".Button_block_2cQNN").click() # CLICAR NO BOTÃO DE LOGIN E FAZER LOGIN


################################################# SESSÃO DENTRO DO HUGGY, ACESSANDO ATÉ A TROCA DO FLOW ##################################################

        #self.driver.find_element(By.CSS_SELECTOR, ".company_3lFvn:nth-child(2)").click()     # CLILCAR NA CONTA DA BRA
        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR EM CONFIGURAÇÕES
        #self.driver.find_element(By.CSS_SELECTOR, ".pz_settings").click()      # CLICAR EM CONFIGURAÇÕES

        #element = self.driver.find_element(By.CSS_SELECTOR, "#menubar-config > .module_3KJrf")     # EFEITOS DA PÁGINA
        #actions = ActionChains(self.driver)    # EFEITOS DA PÁGINA
        #actions.move_to_element(element).perform() # EFEITOS DA PÁGINA
        #element = self.driver.find_element(By.LINK_TEXT, "Canais") # EFEITOS DA PÁGINA
        #actions = ActionChains(self.driver) # EFEITOS DA PÁGINA
        #actions.move_to_element(element).perform() # EFEITOS DA PÁGINA

        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR EM CANAIS
        #self.driver.find_element(By.LINK_TEXT, "Canais").click()     # CLILCAR EM CANAIS
        
        #element = self.driver.find_element(By.CSS_SELECTOR, "body") # EFEITOS DA PÁGINA
        #actions = ActionChains(self.driver) # EFEITOS DA PÁGINA
        #actions.move_to_element(element, 0, 0).perform() # EFEITOS DA PÁGINA

        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        #self.driver.find_element(By.CSS_SELECTOR, ".col-lg-6:nth-child(7) .channel_1WciL").click()   # CLICAR EM WHATS BUSINESS API
        #self.driver.switch_to.frame(1) # RENDERIZA 1 FRAME PARA A EXECUÇÃO
        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        #self.driver.find_element(By.CSS_SELECTOR, ".htable-line").click()    # CLICAR EM WHATS VERIFICADO
        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        #self.driver.find_element(By.CSS_SELECTOR, ".form-item:nth-child(9) .ms-choice > span").click()    # CLICAR NO SELECIONADOR DE FLOW DE SAÍDA
        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA
        #self.driver.find_element(By.CSS_SELECTOR, ".selected:nth-child(1) span").click()    # CLICAR EM NENHUM FLOW DEFINIDO
        #timme.sleep(1) # ESPERA 1 SEGUNDOS ANTES DE CLILCAR NO INPUT A SENHA 
        #self.driver.find_element(By.CSS_SELECTOR, ".hgs-right > .btn").click()    # CLILCAR EM SALVAR
        #self.driver.close()        # FECHA O NAVEGADOR
# FINISH
        

bot = ChromeAutenticao() # INSTANCIAR A CLASSE
bot.ColocarFlow() # INSTANCIAR A FUNÇÃO DENTRO DA CLASSE
