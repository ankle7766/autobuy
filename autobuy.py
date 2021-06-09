from selenium import webdriver
from selenium.webdriver.support.ui import Select

# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 
import time


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.myfone.com.tw/buy/prod/P0000203329344')
driver.find_element_by_link_text('登入').click()

username = "pan7766118@gmail.com"
password = "wildlife1"
driver.implicitly_wait(5)
elem = driver.find_element_by_id('account')
elem.send_keys(username)
elem = driver.find_element_by_id('password')
elem.send_keys(password)

driver.implicitly_wait(3)

driver.find_element_by_class_name("btn-brand-orange").click()
driver.implicitly_wait(2)
driver.find_element_by_class_name("cart-btn").click()
driver.implicitly_wait(4)
driver.find_element_by_id("header_cart").click()
driver.implicitly_wait(4)
driver.find_element_by_id("radio3").click()
driver.implicitly_wait(2)
driver.find_element_by_class_name("nextStep").click()

driver.implicitly_wait(2)
v1 = '1234'
v2 = '2345'
v3 = '3456'
v4 = '4567'
visa1 = driver.find_element_by_id('visa1')
visa1.send_keys(v1)
visa1 = driver.find_element_by_id('visa2')
visa1.send_keys(v2)
visa1 = driver.find_element_by_id('visa3')
visa1.send_keys(v3)
visa1 = driver.find_element_by_id('visa4')
visa1.send_keys(v4)

month = driver.find_element_by_id('cardExpireMonth')
Select(month).select_by_visible_text('02')
year = driver.find_element_by_id('cardExpireYear')
Select(year).select_by_visible_text('2021')
codeinput = '123'
code = driver.find_element_by_id('codenum')
code.send_keys(codeinput)

name = driver.find_element_by_id('username')
name.send_keys('潘冠儒')

uidf = driver.find_element_by_id('uidFirst')
uidf.send_keys('T12318')
uidl = driver.find_element_by_id('uidLast')
uidl.send_keys('4300')

birthyear = driver.find_element_by_id('birthYear')
Select(birthyear).select_by_visible_text('1988')
birthmon = driver.find_element_by_id('birthMonth')
Select(birthmon).select_by_visible_text('06')
birthdate = driver.find_element_by_id('birthDate')
Select(birthdate).select_by_visible_text('06')
driver.implicitly_wait(1)
mail = driver.find_element_by_id('email')
mail.send_keys('ppan7766118@gmail.com')

phone = driver.find_element_by_id('mobile')
phone.send_keys('0987708088')

addcity = driver.find_element_by_id('addrCity')
Select(addcity).select_by_visible_text('屏東縣')
adddist = driver.find_element_by_id('addrDist')
Select(adddist).select_by_visible_text('泰武鄉')
address = driver.find_element_by_class_name('pop_ipt_address')
address.send_keys('佳平村49號')

driver.find_element_by_id("receiverCheckbox").click()
driver.find_element_by_id("paymentVo.defaultSave").click()
# //*[@id="radio3"] uidLast addrDist
# //*[@id="header_cart"]/a //*[@id="pop_oper"]/a[2]/img
# //*[@id="visa1"]
# //*[@id="visa2"]
# //*[@id="visa3"] paymentVo.defaultSave
# //*[@id="visa4"]
# //*[@id="cardExpireMonth"]


# //*[@id="login-form"]/div/div[2]/a