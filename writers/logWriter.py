
def updateTotals():
    cov_Counter = 0
    mystic_Counter = 0
    SSCounter = 0

    outString = "------------OVERALL STATS-------------\n"
    fin = open("logs/temp.log", "r")
    for s in fin.readlines():
        if "Covenant Bookmarks: " in s:
            split = s.split(" ")
            cov_Counter += int(split[2])
        elif "Mystic Bookmarks: " in s:
            split = s.split(" ")
            mystic_Counter += int(split[2])
        elif "SkyStones Spent: " in s:
            split = s.split(" ")
            SSCounter += int(split[2])
    fin.close()

    outString += "Total Covenant Bookmarks: " + str(cov_Counter) + "\n"
    outString += "Total Mystic Bookmarks: " + str(mystic_Counter) + "\n"
    outString += "Total SkyStones Spent: " + str(SSCounter) + "\n"
    outString += "--------------------------------------"

    fout = open("logs/totalStats.log", "w")
    fout.write(outString)
    fout.close()

def writeLog(totalStats):
    try:
        print("Attempting to open 'temp.log'")
        file = open("logs/temp.log", "x")
        print("File does not exist, creating 'temp.log'")
        file.write(totalStats[2:])
    except:
        print("File already exists, appending to file instead")
        file = open("temp.log", "a")
        file.write(totalStats)
    finally:
        file.close()