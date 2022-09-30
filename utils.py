import win32api, win32con
import pyautogui
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def findAndClick(Loc, SleepTime, c, clicks = 1):
    POS = pyautogui.locateCenterOnScreen(Loc, confidence = c)
    try:
        if(POS != None):
            for i in range(clicks):
                click(POS[0], POS[1])
                time.sleep(0.5)
            time.sleep(SleepTime)
            return True
        else:
            return False
    except:
        print("Can't find {}".format(Loc))
        return False

__package__