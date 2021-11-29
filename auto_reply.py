import time
from utils import mouseClick, inputText, keyPress


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
