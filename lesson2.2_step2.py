from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1')
x = x_element.text
y_element = browser.find_element_by_id('num2')
y = y_element.text

def sum(x , y):
    return str(int(x)+int(y))
z = sum(x , y)
    



input1=browser.find_element_by_id("dropdown").click()
input2=browser.find_element_by_id("dropdown").send_keys(z)

input3 = browser.find_element_by_css_selector("button.btn").click()


