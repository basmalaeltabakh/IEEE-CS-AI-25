n = int(input())
sumDiv =0 
for i in range(1,n-1):
    if(n%i == 0):
        sumDiv+=i
if(sumDiv==n):
  print(f"{n}  is a perfect number. ")
else :
     print(f"{n}  is not  a perfect number. ")