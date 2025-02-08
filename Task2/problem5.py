example = open("C:\\Users\\Basmala\\OneDrive\\Desktop\\example.txt", "r")
content = example.read()
words = content.lower().split()
counter = {}
for word in words:
     if word in counter:
       counter[word] += 1  
     else:
        counter[word] = 1  
for word, count in counter.items():
    print(f"{word}: {count}")

example.close()