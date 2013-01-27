# Filename: generate_votes.py
# Author: Lee Xing Mun Jolene
# Index No: 5
# Description: Generate a suitable delimited file VOTES.DAT containing a reasonable
# number of records
# (33,500 votes - 1% spoilt votes, 46% PAP, 43% WP, 6% RP, 4% SDA)

import random

try:
    # open file
    outfile = open("VOTES.DAT", "w")
    
    # generate randomly, splitting according to percentages
    count = 1
    while count != 33501:
        num = random.randint(1,100)
        if num < 47:
            outfile.write("PAP,1\n")
        elif num > 46 and num < 90:
            outfile.write("WP,1\n")
        elif num > 89 and num < 96:
            outfile.write("RP,1\n")
        elif num > 95 and num < 100:
            outfile.write("SDA,1\n")
        else:
            invalid = random.randint(1,4)   # random generation of invalid records
            if invalid == 1:
                outfile.write("PAP,"+str(random.randint(2,9))+"\n")
            if invalid == 2:
                outfile.write("WP,"+str(random.randint(2,9))+"\n")
            if invalid == 3:
                outfile.write("RP,"+str(random.randint(2,9))+"\n")
            if invalid == 4:
                outfile.write("SDA,"+str(random.randint(2,9))+"\n")
        count += 1

    outfile.close() # close file

except IOError:
    print("Error in creating file VOTES.DAT")

