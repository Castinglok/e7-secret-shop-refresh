
def updateTotals():
    cov_Counter = 0
    mystic_Counter = 0
    SSCounter = 0

    outString = "------------OVERALL STATS-------------\n"
    fin = open("temp.log", "r")
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

    fout = open("totalStats.log", "w")
    fout.write(outString)
    fout.close()