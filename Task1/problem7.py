import math
n = int(input())

while n % 2 == 0:
    print(2, end=" ")
    while n % 2 == 0:
       n //= 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        print(i, end=" ")
        while n % i == 0:
          n //= i

