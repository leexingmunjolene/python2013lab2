# Filename: by_election.py
# Author: Lee Xing Mun Jolene
# Index No: 5
# Description: display the by election results which should look similar to the following:

##     DATE: DD/MM/YYYY                 TIME: HH:MM AM/PM
##     RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION
##     WARD                PARTY     #VOTES    %VOTES
##     --------------------------------------------------
##     PUNGGOL EAST SMC    PAP        99999    99.99%
##                         RP         99999    99.99%
##                         SDA        99999    99.99%
##                         WP         99999    99.99%
##     --------------------------------------------------
##     WINNER: <Party with highest percentage of votes>
##     TOTAL VOTES: 
##     #SPOILT VOTES:
##     %SPOLIT VOTES:

import datetime

try:
    infile = open("VOTES.DAT", "r") # open file for reading
    outfile = open("RESULTS.TXT", "w")  # open file for writing

    lines = infile.readlines()  # count votes
    PAP = 0
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

    dt = datetime.datetime.now()    # get current date and time

    if PAP > WP and PAP > RP and PAP > SDA: # detemine winner
        winner = "PAP"
    elif WP > PAP and WP > RP and WP > SDA:
        winner = "WP"
    elif RP > PAP and RP > SDA and RP > WP:
        winner = "RP"
    else:
        winner = "SDA"

    # output to screen
    print("{0:<25}".format("DATE: "+str(dt.strftime("%d/%m/%Y")))+  # format date
          "{0:>25}".format("TIME: "+str(dt.strftime("%I:%M %p"))))  # format time
    print("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION")
    print("{0:<20}".format("WARD")+"{0:<10}".format("PARTY")+
          "{0:<10}".format("#VOTES")+"{0:<10}".format("%VOTES"))
    print("-"*50)
    print("{0:<20}".format("PUNGGOL EAST SMC")+"{0:<10}".format("PAP")+
          "{0:<10}".format(str(PAP))+"{0:<10}".format(str("{0:.2f}".format(PAP/len(lines)*100))+"%"))
    print("{0:<20}".format("")+"{0:<10}".format("RP")+
          "{0:<10}".format(str(RP))+"{0:<10}".format(str("{0:.2f}".format(RP/len(lines)*100))+"%"))
    print("{0:<20}".format("")+"{0:<10}".format("SDA")+
          "{0:<10}".format(str(SDA))+"{0:<10}".format(str("{0:.2f}".format(SDA/len(lines)*100))+"%"))
    print("{0:<20}".format("")+"{0:<10}".format("WP")+
          "{0:<10}".format(str(WP))+"{0:<10}".format(str("{0:.2f}".format(WP/len(lines)*100))+"%"))
    print("-"*50)
    print("WINNER: " + winner)
    print("TOTAL VOTES: "+str(len(lines)))
    print("#SPOILT VOTES: "+str(invalid))
    print("%SPOILT VOTES: "+str("{0:.2f}".format(invalid/len(lines)*100))+"%")

    # output to file RESULTS.TXT
    outfile.write("{0:<25}".format("DATE: "+str(dt.strftime("%d/%m/%Y")))+
          "{0:>25}".format("TIME: "+str(dt.strftime("%I:%M %p")))+"\n")
    outfile.write("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION"+"\n")
    outfile.write("{0:<20}".format("WARD")+"{0:<10}".format("PARTY")+
          "{0:<10}".format("#VOTES")+"{0:<10}".format("%VOTES")+"\n")
    outfile.write("-"*50+"\n")
    outfile.write("{0:<20}".format("PUNGGOL EAST SMC")+"{0:<10}".format("PAP")+
          "{0:<10}".format(str(PAP))+"{0:<10}".format(str("{0:.2f}".format(PAP/len(lines)*100))+"%\n"))
    outfile.write("{0:<20}".format("")+"{0:<10}".format("RP")+
          "{0:<10}".format(str(RP))+"{0:<10}".format(str("{0:.2f}".format(RP/len(lines)*100))+"%\n"))
    outfile.write("{0:<20}".format("")+"{0:<10}".format("SDA")+
          "{0:<10}".format(str(SDA))+"{0:<10}".format(str("{0:.2f}".format(SDA/len(lines)*100))+"%\n"))
    outfile.write("{0:<20}".format("")+"{0:<10}".format("WP")+
          "{0:<10}".format(str(WP))+"{0:<10}".format(str("{0:.2f}".format(WP/len(lines)*100))+"%\n"))
    outfile.write("-"*50+"\n")
    outfile.write("WINNER: "+winner+"\n")
    outfile.write("TOTAL VOTES: "+str(len(lines))+"\n")
    outfile.write("#SPOILT VOTES: "+str(invalid)+"\n")
    outfile.write("%SPOILT VOTES: "+str("{0:.2f}".format(invalid/len(lines)*100))+"%")

    
    infile.close()  # close file
    outfile.close()

except ZeroDivisionError or IOError:
        print("Error reading VOTES.DAT or writing to RESULTS.TXT")
