n = int(input("number of terms:")) 
a = 0 
b = 1 
if n >= 1: 
    print(a, end=" ") 
if n >= 2: 
    print(b, end=" ") 
for i in range(2, n): 
    next_term = a + b 
    print(next_term, end=" ") 
    a, b = b, next_term 
