import pyautogui
import webbrowser
from time import sleep

url = "https://www.crazygames.com.br/jogos/doge-miner-2"
webbrowser.open(url)
sleep(4)
pyautogui.moveTo(1412, 701, duration=2)
sleep(11)
pyautogui.click()
pyautogui.moveTo(960, 581, duration=2)
pyautogui.click()
sleep(8)
pyautogui.click()
pyautogui.moveTo(1014, 566, duration=2)
pyautogui.click()
pyautogui.moveTo(817, 460, duration=2)
sleep(16)
for i in range(599):
    pyautogui.click()
