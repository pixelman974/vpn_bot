import pyautogui
import time

print("У тебя 5 секунд, чтобы навести мышку на кнопку 'Приступим'...")

time.sleep(5)

print("Текущая позиция курсора:", pyautogui.position())
