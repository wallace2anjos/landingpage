from selenium import webdriver #pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from openpyxl import Workbook
import re

import time

chrome = 'C:/webdrivers/chromedriver.exe' #path for chrome driver
email = input('Escreva o endereço do gmail para login: ')
password = input('Escreva a Senha do gmail para login: ')
driver = webdriver.Chrome(chrome)
delay = 6
logged = False
new_email = True
book = Workbook()
sheet = book.active
rows = []


driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
next = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span'

driver.find_element_by_name('identifier').send_keys(email)
driver.find_element_by_xpath(next).click()

mail_list_email = []
mail_list_content = []
while logged == False:
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'password')))
        print("Page is ready!")
        time.sleep(0.5)
        driver.find_element_by_name('password').send_keys(password)
        logged = True
        break
    except TimeoutException:
        print("Loading took too much time!")
        time.sleep(5)
        print("Waiting 5 seconds")

print('loop break')
driver.find_element_by_xpath(next).click()
time.sleep(5)

num_emails = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/span/div[1]/span/span[2]')
print(f'got value {num_emails}')
num_emails = num_emails.text
num_emails = re.sub(r'[^\w\s]', '', num_emails)
print(f'inbox mails {num_emails}')
print(num_emails)
for i in range(0, int(num_emails)):
    print(f'entrou no for{i}')
    while new_email == True:

        try:
            # CLIQUE NO EMAIL MAIS RECENTE
            print(f'entrou no try{i}')
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/table/tbody/tr[1]')))
            print('Waiting')
            try:
                print(f'entrou no try{i}.1')
                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/table/tbody/tr[1]').click()
                print('clicou no email da caixa de entrada')
            except:
                print(f'entrou no except{i}.1')
                break

            try:
                # COPIA O EMAIL
                mail_list_content.clear()
                print(f'entrou no try{i}.2')
                time.sleep(1)
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]/table/tbody/tr/td/h3/span/span')))
                #element = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]/table/tbody/tr/td/h3/span/span')
                print('atribuiu element')

                try:
                    print(f'entrou no try{i}.2.1')
                    element_nome_email_tel = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div')

                except:
                    print(f'entrou no except{i}.2.1')

                    try:
                        print(f'entrou no try{i}.2.2')
                        element_nome_email_tel = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div')
                    except:
                        print(f'entrou no except{i}.2.2')

                        try:
                            print(f'entrou no try{i}.2.3')
                            element_nome_email_tel = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div')
                        except:
                            print(f'entrou no except{i}.2.3')
                            break
                        break
                    break
                #print(element.text) #email de contato
                print(element_nome_email_tel.text) #formulário de contato
                tratando = element_nome_email_tel.text
                print('sem quebra', tratando)
                tratando = str(tratando.replace("\\n", " "))
                print(tratando)
                tratando = str(tratando.replace("Nome: ", "$"))
                print(tratando)
                tratando = str(tratando.replace("E-mail: ", "$"))
                print(tratando)
                tratando = str(tratando.replace("Telefone: ", "$"))
                print(tratando)
                tratando = str(tratando.replace("Formulário enviado por ", "$"))
                print(tratando)
                tratando = str(tratando.replace(" no Website http://vencendogigantes.josuevalandro.com.br/: ", "$"))
                print(tratando)
                tratando = str(tratando.replace(" $", ":"))
                tratando = str(tratando.replace(" $", ":"))
                print(tratando)
                tratando = str(tratando.replace("\n", ""))
                # tratando = str(tratando.replace(":", "$"))
                tratando = tratando.split("$")
                print(tratando)
                print(tratando[-1])
                print(tratando[-2])
                print(tratando[-3])
                #mail_list_email.append(element)
                mail_list_content.append(tratando[-1])
                mail_list_content.append(tratando[-2])
                mail_list_content.append(tratando[-3])
                print(mail_list_content)

                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]').click()
                sheet.append(mail_list_content)
                book.save('mail_list.xlsx')
                break

            except TimeoutException:
                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]').click()
                print("Loading took too much time!")
                time.sleep(5)

        except TimeoutException:
            print("Loading took too much time!")
            time.sleep(5)


# gmailExit = False
# while not gmailExit:
#    login()
