#Adding random
import random

#This produces the magic (the choices for the PLD)
def pld_choices(data):
    
    #define choice to store picks
    choices = [0, 0]
    from operator import itemgetter
    
    #get total score of PLD people
    print("**************************************************")
    print("SORT COMPLETE...")
    print("**************************************************")
    data.sort(key=itemgetter(4))
    print(data)

    #getting half of array data size, then halfing again 
    # to get Lead and Assitant based on sorted weight
    sizeof = len(data)
    half = sizeof / 2
    choices[0] = random.randrange(half-1)
    choices[1] = random.randrange(half, sizeof)

    return choices