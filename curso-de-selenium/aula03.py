
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser =Firefox()
browser.get(url)
sleep(3)
#a = browser.find_element_by_tag_name('a')
#a=browser.find_element(By.TAG_NAME, 'a')
a = browser.find_element(By.LINK_TEXT, 'minha ancora')
#p=browser.find_element(By.TAG_NAME, 'p')
#a.text
#p.text
#print(f'texto de a: {a.text}')
#print(f'texto de p: {p.text}')
for click in range(10):
    ps = browser.find_elements(By.TAG_NAME, 'p')
    a.click()
    print(f'Valor do ultimo p: {ps[-1].text} valor do click: {click}')

    print(f'Os valors são iguais {ps[-1].text == str(click)}')

#browser.quit()
