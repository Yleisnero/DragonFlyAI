import time
import pyautogui


def dive(duration):
    pyautogui.keyDown('left')
    print("dive\n")
    time.sleep(duration)
    pyautogui.keyUp('left')
    print("don't dive\n")


if __name__ == '__main__':
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width/2, screen_height/2, duration=1)
    pyautogui.click()
    for x in range(10):
        dive(1)
        time.sleep(1)
