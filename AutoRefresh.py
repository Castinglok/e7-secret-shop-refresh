from writers.logWriter import *
from pyautogui import *
import pyautogui
import time
import datetime
import keyboard
import win32api, win32con

#starting time
startDT = datetime.datetime.now()

#counters
cov_Counter = 0
mystic_Counter = 0
SSCounter = 0

#sleep timers
SleepTime = 0.5


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(SleepTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def printStats():
    currDT = datetime.datetime.now()

    totalStats = "\n\n----------BOOKMARKS BOUGHT------------\n"
    totalStats += currDT.strftime("%x") + " " + currDT.strftime("%X") + "\n"
    totalStats += "Elapsed Time: " + str(currDT - startDT) + "\n"
    totalStats += "Covenant Bookmarks: " + str(cov_Counter) + "\n"
    totalStats += "Mystic Bookmarks: " + str(mystic_Counter) + "\n"
    totalStats += "SkyStones Spent: " + str(SSCounter) + "\n"
    totalStats += "--------------------------------------"

    writeLog(totalStats)
    print(totalStats[1:])

#first click to minimize ide
click(1810,14)

#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590


while keyboard.is_pressed('q') == False:
    
    RB_pos=pyautogui.locateOnScreen('pictures/refresh_button.png')
#The confidence is added due to little variations in the background
    Coven_pos=pyautogui.locateOnScreen('pictures/covenant.png',confidence=0.95)
    Mystic_pos=pyautogui.locateOnScreen('pictures/mystic.png',confidence=0.95)
    time.sleep(SleepTime)
#Checks for covenant
    if (Coven_pos) != None:
        time.sleep(SleepTime)
        print("Buy Covenant Summons.")
        try:
            Coven_point=pyautogui.center(Coven_pos)
            click(Coven_point[0]+800, Coven_point[1]+50)
            click(Coven_point[0]+800, Coven_point[1]+50)
        except:
            printStats()
            updateTotals()
        time.sleep(SleepTime)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('pictures/Buy_button_Covenant.png')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        cov_Counter += 5
        time.sleep(SleepTime)
    else:
        print("No Covenant summons to buy.")       

#checks for mystic
    if (Mystic_pos) != None:
        time.sleep(SleepTime)        
        print("Buy Mystic Summons.")
        try:
            Mystic_point=pyautogui.center(Mystic_pos)
            click(Mystic_point[0]+800, Mystic_point[1]+50)
            click(Mystic_point[0]+800, Mystic_point[1]+50)
        except:
            printStats()
            updateTotals()
        time.sleep(SleepTime)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('pictures/Buy_button_Mystic.png')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        mystic_Counter += 50
        time.sleep(SleepTime)
    else:
        time.sleep(SleepTime)
        print("No Mystic summons to buy.")
        click(x=1263,y=590)
    
    pyautogui.scroll(-5, x=1263, y=590)
    time.sleep(1)
    Coven_pos2=pyautogui.locateOnScreen('pictures/covenant.png',confidence=0.95)
    Mystic_pos2=pyautogui.locateOnScreen('pictures/mystic.png',confidence=0.95)
	
#break point check to close macro
    if(keyboard.is_pressed('q')):
        break   

#Checks for covenant
    if (Coven_pos2) != None:
        time.sleep(SleepTime)
        print("Buy Covenant Summons.")
        try:
            Coven_point=pyautogui.center(Coven_pos2)
            click(Coven_point[0]+800, Coven_point[1]+50)
            click(Coven_point[0]+800, Coven_point[1]+50)
        except:
            printStats()
            updateTotals()
        time.sleep(SleepTime)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('pictures/Buy_button_Covenant.png')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        cov_Counter += 5
        time.sleep(SleepTime)
    else:
        print("No Covenant summons to buy.")
        
#checks for mystic
    if (Mystic_pos2) != None:
        time.sleep(SleepTime)        
        print("Buy Mystic Summons.")
        try:
            Mystic_point=pyautogui.center(Mystic_pos2)
            click(Mystic_point[0]+800, Mystic_point[1]+50)
            click(Mystic_point[0]+800, Mystic_point[1]+50)
        except:
            printStats()
            updateTotals()
        time.sleep(SleepTime)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('pictures/Buy_button_Mystic.png')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        mystic_Counter += 50
        time.sleep(SleepTime)
    else:
        print("No Mystic summons to buy.")
        click(x=1263,y=590)

#break point check to close macro
    if(keyboard.is_pressed('q')):
        break    
    
#Finally refreshes
    RB_point=pyautogui.center(RB_pos)
    click(RB_point[0], RB_point[1])
    click(RB_point[0], RB_point[1])
    time.sleep(SleepTime)#wait for confirm to appear
    Confirm_pos=pyautogui.locateOnScreen('pictures/confirm button.png')
    try:
        Confirm_point=pyautogui.center(Confirm_pos)
        click(Confirm_point[0], Confirm_point[1])
        click(Confirm_point[0], Confirm_point[1])
        SSCounter += 3
    except:
        printStats()
        updateTotals()
    time.sleep(SleepTime)

#print stats at end
printStats()
updateTotals()