import os
import time
import pyautogui

def start_amnezia_vpn_windows():
    path = r"C:\Program Files\AmneziaVPN\AmneziaVPN.exe"  # Убедись, что путь верный
    os.startfile(path)
    print("Amnezia VPN запущен")

    # Ждём загрузку окна (можно изменить задержку)
    time.sleep(5)

    pyautogui.click(x=935, y=834)  # ← Измени координаты под кнопку "3 соединения"
    print("Кнопка '3 соединения' нажата")

    pyautogui.click(x=953, y=408)
    print('Кнопка нажата')

    pyautogui.scroll(-200)
    print('Скрол выполнен')

    pyautogui.click(x=959, y=738)  # ← Измени координаты под кнопку "Поделиться 2"
    print("Кнопка 'Поделиться' нажата")

    time.sleep(10)

    pyautogui.click(x=965, y=403)  # ← Измени координаты под кнопку "Приступим"
    print("Кнопка 'Скопировать' нажата")

    # Закрытие AmneziaVPN
    time.sleep(10)
    os.system('taskkill /f /im AmneziaVPN.exe')
    print("Amnezia VPN закрыт")

if __name__ == "__main__":
    start_amnezia_vpn_windows()
