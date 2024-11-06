#takes the input from the user 
a = input("enter a word or number =")
# condition for checking the palindrome 
b = a[::-1]
if a == b:
    print(f"the given {a} is a plindrome number")
else :
    print(f"the {a} is not a palindrome")    
