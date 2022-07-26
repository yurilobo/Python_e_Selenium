#Aula 4
#busca aninhada,Atributos e navegação
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
browser=Firefox()
browser.get('https://curso-python-selenium.netlify.app/aula_04_a.html')

lista_n_ordenada=browser.find_element(By.TAG_NAME, 'ul')
lis=lista_n_ordenada.find_elements(By.TAG_NAME, 'li')
#browser
