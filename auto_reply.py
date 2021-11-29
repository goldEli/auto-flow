import time
import pyautogui

#
# pyautogui.moveTo(100, 150)

# pyautogui.alert('This is an alert box.')


def mouseClick(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y,
                            button="left", interval=0.2)
            return True
        time.sleep(0.1)


def inputText(text):
    pyautogui.write(text, interval=0.25)


def keyPress(key):
    pyautogui.press(key)


if __name__ == '__main__':
    mouseClick("./imgs/wechat_icon.jpg")
    isWait = False
    while True:
        time.sleep(0.5)
        if isWait == True:
            continue
        res = mouseClick("./imgs/note_icon.jpg")
        if res == True:
            inputText("auto replay")
            keyPress('enter')
