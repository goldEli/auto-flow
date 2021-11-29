from time import time
import pyautogui


def mouseClick(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y,
                            button="left", interval=0.2)
            break
        time.sleep(0.1)


def inputText(text):
    pyautogui.write(text, interval=0.25)

def keyPress(key):
		pyautogui.press(key)