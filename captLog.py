#This file will input the number of people who has
def cap_log(name):
    print("Number of people helped by " + name)
    numPeople = int(input())
    value = 10 / (1 + numPeople*numPeople)
    return value 
