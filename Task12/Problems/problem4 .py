import numpy as np
# create a 2D array of size n * n 
while True:
    try:
        n = int(input("Enter a number for the size of the array: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

 # first solution 
arr = np.arange(1, n + 1)   # [1, 2, ..., n]
arr = np.tile(arr, (n, 1))  # Repeat it n times vertically

print(" Array 1 " , arr)
print ("#" * 30)

# second solution 
arr = np.zeros((n, n), dtype=int)

for i in range(n):
    arr[:, i] = i + 1  
print("Array 2 " ,  arr)

