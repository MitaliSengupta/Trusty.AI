#This file is to store the funtion of getting student names

#calling data matrix from main
import getVar

#getting student name index from matrix
def getSname():
    name = input()
    a = 0
    while a < 6:
        if name == getVar.data[a][0]:
            return (a)
        a += 1