#This file will convert the input into average

#import functions 
import functions
#import variables and matrix
import getVar


sname = functions.getSname()
voteCount = 0
i = 0
while i < 6:
    #getting vote average
    vote = input()
    #BC
    voteAvg = float
    voteAvg = (voteAvg * voteCount + vote) / (voteCount + 1)
    voteCount += 1
    getVar.data[sname][1] = (getVar.data[sname][1] * getVar.data[sname][2] + voteAvg) / (getVar.data[sname][2] + 1)
    getVar.data[sname][2] += 1
    i += 1