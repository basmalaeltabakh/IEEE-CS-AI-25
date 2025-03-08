from fractions import Fraction
def conditionalProbability(eventA, eventB):
    countA = 0          
    countAandB = 0    
   
    for i in range(len(eventA)):
        if eventA[i] == 1:
            countA += 1
            if eventB[i] == 1:
                countAandB += 1 

    return Fraction(countAandB, countA) if countA > 0 else Fraction(0, 1)

event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]
print(conditionalProbability(event_a, event_b))  
