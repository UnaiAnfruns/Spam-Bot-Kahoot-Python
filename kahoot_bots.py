from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import names
import os

#MAIN VARIABLES
window = 1
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m".format(skk))
def prYellow(skk): print("\033[93m{}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m{}\033[00m".format(skk))
def prPurple(skk): print("\033[95m{}\033[00m".format(skk))
def prCyan(skk): print("\033[96m{}\033[00m".format(skk))
def prLightGray(skk): print("\033[97m{}\033[00m".format(skk))
def prBlack(skk): print("\033[98m{}\033[00m".format(skk))

pin = "7848146"
#bots = 20
def Kahoot_FristTab(pin,driver):
    driver.get("https://kahoot.it/")
    pin_input = driver.find_element(By.XPATH, '//*[@id="game-input"]')
    pin_input.send_keys(pin)
    pin_button = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button')
    pin_button.click()
    while True:
        try:
            name_input = driver.find_element(By.XPATH, '//*[@id="nickname"]')
            if (len(str(name_input))) > 4:
                break
        except:
            pyautogui.sleep(1)
    pyautogui.sleep(0.5)
    random_name = names.get_first_name()
    ################################
    #CHANGE NAME IF YOU WANT ANOTHER#
    ################################
    name_input.send_keys("1. AINS")
    pin_button = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div[1]/div[3]/div[2]/main/div/form/button')
    pin_button.click()
def Kahoot_NewTab(pin,driver,window):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[window])
    driver.get("http://kahoot.it")
    #
    while True:
        try:
            pin_input = driver.find_element(By.XPATH, '//*[@id="game-input"]')
            if (len(str(pin_input))) > 4:
                break
        except:
            pyautogui.sleep(0.5)
    #
    pin_input.send_keys(pin)
    pin_button = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button')
    pin_button.click()
    while True:
        try:
            name_input = driver.find_element(By.XPATH, '//*[@id="nickname"]')
            print(name_input)
            if (len(str(name_input))) > 4:
                break
        except:
            pyautogui.sleep(1)
    pyautogui.sleep(0.5)
    random_name = names.get_first_name()
    ################################
    #CHANGE NAME IF YOU WANT ANOTHER#
    ################################
    ains_name = "{}. AINS".format((window+1))
    name_input.send_keys(ains_name)
    pin_button = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div[1]/div[3]/div[2]/main/div/form/button')
    pin_button.click()
    window += 1
    return window

if __name__ == '__main__':
    os.system('cls')
    prPurple("""
|/ _ |_  _  _ _|_
|\(_|| |(_)(_) | 
    """)
    pin = str(input("Introduce el pin de la sala : "))
    bots = int(input("Introduce la cantidad de bots que quieres introducir (Maximo 20 Bots): "))
    driver = webdriver.Firefox()
    Kahoot_FristTab(pin,driver)
    for x in range(0,bots-1):
        window = Kahoot_NewTab(pin,driver,window)




