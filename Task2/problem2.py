n = int(input())
scores = list(map(int, input().split()))
    
scores = set (scores)
sortedScores = sorted(scores,reverse=True)    

secondMax = sortedScores[1]
print(secondMax)
