def probabilityDistribution(data):
    total = len(data)
    freq = {}  
    for num in data:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    probabilities = {}

    for key in freq:
        probabilities[key] = freq[key] / total
        
    return probabilities


data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
print(probabilityDistribution(data))
