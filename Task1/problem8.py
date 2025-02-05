word =  str (input())
palindrome = True
left = 0 
right = len(word) - 1 
while left < right:
    if word[left] != word[right]:
        palindrome = False
    left+=1
    right-=1
if palindrome :
    print (f"The word {word} is a palindrome")
else:
    print (f"The word {word} is not a palindrome")


