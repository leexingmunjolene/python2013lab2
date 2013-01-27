# Filename: count_votes.py
# Author: Lee Xing Mun Jolene
# Index No: 5
# Description: Count the number and percentage of votes garnered by each party

try:
    infile = open("VOTES.DAT", "r") # open file for reading
    lines = infile.readlines()
    
    PAP = 0     # count votes
    WP = 0
    RP = 0
    SDA = 0
    invalid = 0
    for line in lines:
        line = line.rstrip('\n')
        if line == 'PAP,1':
            PAP += 1
        elif line == 'WP,1':
            WP +=1
        elif line == 'RP,1':
            RP += 1
        elif line == 'SDA,1':
            SDA += 1
        else:
            invalid += 1

    print("PAP has garnered "+str(PAP)+" votes, which is "+str("{0:.2f}".format(PAP/len(lines)*100))+"% of the total votes.")
    print("WP has garnered "+str(WP)+" votes, which is "+str("{0:.2f}".format(WP/len(lines)*100))+"% of the total votes.")
    print("RP has garnered "+str(RP)+" votes, which is "+str("{0:.2f}".format(RP/len(lines)*100))+"% of the total votes.")
    print("SDA has garnered "+str(SDA)+" votes, which is "+str("{0:.2f}".format(SDA/len(lines)*100))+"% of the total votes.")
    print(str(invalid)+" votes, which is "+str("{0:.2f}".format(invalid/len(lines)*100))+"% of the total votes are spoilt votes.")

    infile.close()  # close file

except IOError:
    print("Error finding or opening VOTES.DAT")
