a = int(input("enter a number ="))
b = int(input("enter b number ="))
n = input("enter the required calcultion symbol '+','-','*','%','//' ")
def add_2_numbers(a,b):
    if n == "+":
        sum = a+b
        print("the sum of 2 numbers is =",sum)
    elif n == "-":
        sub = a - b
        print("the subtraction of 2 numbers is =",sub)
    elif n == "*":
        multiply = a * b
        print("the product of 2 numbers is =",multiply)
    elif n == "%":
        division = a % b
        print("the division of 2 numbers id =",division)
    elif n == "//":
        floor_division = a//b
        print("the floor division of 2 numbers =",floor_division)
    else :
        print("invlid input")
(add_2_numbers(a,b))                    

    
