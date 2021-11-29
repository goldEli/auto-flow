import pyautogui

#
# pyautogui.moveTo(100, 150)

# pyautogui.alert('This is an alert box.')

if __name__ == '__main__':
    # key = input('select：1.once 2.Infinite loop\n')
		screenWidth, screenHeight = pyautogui.size()
		print("screen size", screenWidth, screenHeight)
		location = pyautogui.locateCenterOnScreen(
		    "./imgs/chrome_icon.jpg", confidence=0.9)
		if location is not None:
			pyautogui.click(location.x,location.y,button="left")

    # print(key)

# print(screenWidth, screenHeight)
