#This function will get total score 
def exer_score(name):
    print("Enter average exercise score for " + name)
    totalScore = int(input())
    value = 10/((totalScore/50)**2 + 1)
    return value 