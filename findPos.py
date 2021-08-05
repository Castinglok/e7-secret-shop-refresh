import pyautogui;

#x=378, y=957
Coven_pos=pyautogui.locateOnScreen('confirm button.png')

print(pyautogui.center(Coven_pos))