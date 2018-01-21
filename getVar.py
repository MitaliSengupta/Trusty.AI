#seed data

i, n = 6, 6
data = [[0 for x in range(i)] for y in range(n)]
for i in range(6):
    #Student Names
    data[i][0] = input()

    #PLD average
    pldAv = float
    data[i][1] = pldAv
    #Number of PLD
    numPld = int
    data[i][2] = numPld

    #Average of project excercise before PLD
    avgExc = float
    data[i][3] = avgExc