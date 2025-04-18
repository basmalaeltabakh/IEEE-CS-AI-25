import numpy as np

n = int(input())
arr = np.array(list(map(int , input().split())))

left , right = 0 , n-1
sereja , dima = 0, 0 


Sereja = True

while left <= right:
    if arr[left] > arr[right]:
        chosen = arr[left]
        left += 1
    else:
        chosen = arr[right]
        right -= 1

    if Sereja:
        sereja += chosen
    else:
        dima += chosen

    Sereja = not Sereja

print(sereja, dima) 
