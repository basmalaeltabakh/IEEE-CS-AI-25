def getNumbers():
    try:
        numbers = list(map(int, input("Enter Numbers separated by space: ").split()))
        if not numbers:
            print("List can't be empty. Please enter numbers.")
            return getNumbers()  
        return numbers
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return getNumbers() 

def findMin(numbers):
    minVal = numbers[0]
    for num in numbers :
        if num<minVal:
            minVal = num
    if not numbers:
        return None
    return minVal

def findMax(numbers):
    maxVal = numbers[0]
    for num in numbers :
        if num>maxVal:
            maxVal = num
    if not numbers:
        return None
    return maxVal

def findMean(numbers):
    if not numbers:
        return None
    sum = 0
    for num in numbers:
        sum+=num
    mean = sum / len(numbers)
    return mean

def findMode(numbers):
    if not numbers:
        return None
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    maxFreq = findMax(list(freq.values()))  
    mode = []
    for num, count in freq.items():
        if count == maxFreq:
            mode.append(num)
    return mode


def findMedian(numbers):
    sortedNumbers = sorted(numbers) 
    n = len(sortedNumbers)
    if n % 2 == 0:
        return (sortedNumbers[n//2] + sortedNumbers[(n // 2) - 1]) / 2
    else :
        return sortedNumbers[(n-1)//2]
    
def findRange(numbers):
    if not numbers:
        return None
    return findMax(numbers) - findMin(numbers)

def findVariance(numbers):
    if not numbers:
        return None
    mean = findMean(numbers)
    deviation = 0
    for num in numbers:
        deviation += (num - mean) ** 2  
    return deviation / len(numbers)


def findSTD(numbers):
    if not numbers:
        return None
    return findVariance(numbers)** 0.5

def findQuartiles(numbers):
    if not numbers:
        return None
    sortedNumbers = sorted(numbers)
    n = len(sortedNumbers)
    left = sortedNumbers[:n // 2]
    right = sortedNumbers[(n + 1) // 2:]
    Q2 = findMedian(sortedNumbers)
    Q1 = findMedian(left)
    Q3 = findMedian(right)
    return Q1, Q2, Q3

def findIQR(numbers):
    if not numbers:
        return None
    Q1, Q2, Q3 = findQuartiles(numbers)
    return Q3 - Q1

numbers = getNumbers()
if numbers:
    print(f"Min: {findMin(numbers)}")
    print(f"Max: {findMax(numbers)}")
    print(f"Mean: {findMean(numbers):.1f}")
    print(f"Mode: {findMode(numbers)}")
    print(f"Median: {findMedian(numbers)}")
    print(f"Range: {findRange(numbers)}")
    print(f"Variance: {findVariance(numbers):.2f}")
    print(f"Standard Deviation: {findSTD(numbers):.5f}")
    print(f"Quartiles: {findQuartiles(numbers)}")
    print(f"Interquartile Range (IQR): {findIQR(numbers)}")