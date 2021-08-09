import pyautogui
import datetime

currDT = datetime.datetime.now()
cov_Counter = 30
mystic_Counter = 400
SSCounter = 249

totalStats = "\n\n----------BOOKMARKS BOUGHT------------\n"
totalStats += currDT.strftime("%x") + " " + currDT.strftime("%X") + "\n"
totalStats += "Covenant Bookmarks: " + str(cov_Counter) + "\n"
totalStats += "Mystic Bookmarks: " + str(mystic_Counter) + "\n"
totalStats += "SkyStones Spent: " + str(SSCounter) + "\n"
totalStats += "--------------------------------------"

print(totalStats)

# print("----------BOOKMARKS BOUGHT------------")
# print(currDT.strftime("%c"), currDT.strftime("%X"))
# print("Covenant Bookmarks: " + str(cov_Counter))
# print("Mystic Bookmarks: " + str(mystic_Counter))
# print("SkyStones Spent: " + str(SSCounter))
# print("--------------------------------------")



try:
    print("Attempting to open 'temp.log'")
    file = open("temp.log", "x")
    file.write(totalStats)
except:
    print("File already exists, appending to file instead")
    file = open("temp.log", "a")
    file.write(totalStats)
finally:
    file.close()

#x=378, y=957
# print(pyautogui.position())
