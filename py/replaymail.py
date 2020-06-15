from selenium import webdriver #pip install selenium
import time
chrome = 'C:/webdrivers/chromedriver.exe' #path for chrome driver
email = input('Escreva o endereço do gmail para login: ')
password = input('Escreva a Senha do gmail para login: ')
replyBegin = 'Frase de agradecimento '
replyEnd = ' Frase de agradecimento'
textLink = 'clique aqui para baixar'
urlLink = 'http://www.google.com.br'
driver = webdriver.Chrome(chrome)
driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

def login():
    driver.find_element_by_name('identifier').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span').click()
    time.sleep(3)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span').click()
    time.sleep(3)

def reply_email():
    for i in range(0, 1):
        # CLIQUE NO EMAIL MAIS RECENTE
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/table/tbody/tr[1]/td[6]/div/div/div/span/span').click()
        time.sleep(1)

        # CLIQUE NO BOTÃO REPLY
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/table/tbody/tr/td[2]/div/div/span[1]').click()
        time.sleep(1)

        # BEGIN EMAIL
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div/div[1]').send_keys(replyBegin)

        # CLIQUE NO BOTÃO DE INSERIR LINK
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div[2]/div[1]/div[4]/table/tbody/tr/td[4]/div/div[2]/div/div/div').click()
        time.sleep(1)

        driver.find_element_by_id('linkdialog-text').send_keys(textLink)
        driver.find_element_by_id('linkdialog-onweb-tab-input').send_keys(urlLink)
        driver.find_element_by_name('ok').click()

        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div/div[1]').send_keys(replyEnd)
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div[2]/div[1]/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]').click()

        time.sleep(1)

gmailExit = False
while not gmailExit:
    login()
    reply_email()
