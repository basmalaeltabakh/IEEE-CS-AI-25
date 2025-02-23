def sampleStats(count):
    minimum, maximum, mode = -1, -1, 0
    totalSum, totalCount = 0, 0

    for i in range(256):
        if count[i] > 0:
            if minimum == -1:
                minimum = i
            maximum = i
            totalSum += i * count[i]
            totalCount += count[i]
            if count[i] > count[mode]:
                mode = i  

    mean = totalSum / totalCount

    mid1, mid2 = (totalCount - 1) // 2, totalCount // 2
    cumulativeCount, median1, median2 = 0, -1, -1

    for i in range(256):
        cumulativeCount += count[i]
        if median1 == -1 and cumulativeCount > mid1:
            median1 = i
        if median2 == -1 and cumulativeCount > mid2:
            median2 = i
            break

    median = (median1 + median2) / 2.0

    return [float(f"{minimum:.5f}"), float(f"{maximum:.5f}"), float(f"{mean:.5f}"), float(f"{median:.5f}"), float(f"{mode:.5f}")]

userInput = input("Enter numbers: ")  
count = eval(userInput.strip())  
print(sampleStats(count))
