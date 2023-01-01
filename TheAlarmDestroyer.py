from time import sleep
from datetime import datetime
import pyautogui as pag

# Get screen size
screenWidth, screenHeight = pag.size()

# Position of important points on screen
b_ekranglowny = [0.19791666666666666, 0.03148148148148148]
b_alarmy = [0.4973958333333333, 0.6731481481481482]
b_lista = [0.046875, 0.2740740740740741]
b_krytyczny = [0.23020833333333332, 0.20833333333333334]
b_wysoki = [0.3078125, 0.2064814814814815]
b_sredni = [0.378125, 0.20833333333333334]
b_niski = [0.45, 0.2064814814814815]
b_potwierdz = [0.6171875, 0.7620370370370371]


# Function for mouse click
def click(button):
    pag.moveTo(button[0] * screenWidth, button[1] * screenHeight, 3)
    pag.click()
    sleep(1)


# Function for mouse scroll
def scroll(button):
    pag.moveTo(button[0] * screenWidth, button[1] * screenHeight, 3)
    pag.scroll(3000)
    pag.click()
    sleep(1)


# Function for confirm all alarms
def apply():
    click(b_ekranglowny)
    click(b_alarmy)
    scroll(b_lista)
    click(b_krytyczny)
    click(b_potwierdz)
    click(b_wysoki)
    click(b_potwierdz)
    click(b_sredni)
    click(b_potwierdz)
    click(b_niski)
    click(b_potwierdz)
    click(b_ekranglowny)


# Function for call apply function in time peroids
def main():
    sleep(10)
    apply()

    now = datetime.now()
    start = now.replace(hour=6, minute=50, second=0).time()
    stop = now.replace(hour=7, minute=7, second=59).time()
    delay = 900

    while True:
        sleep(delay)
        now = datetime.now()
        if (stop >= now.time() > start) and now.weekday() not in [5, 6]:
            delay = 50
            if now.hour == stop.hour and now.minute == stop.minute:
                delay = 900
                apply()


if __name__ == '__main__':
    main()
