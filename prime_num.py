num = int(input("enter a number = "))
if num > 0:
    for x in range (2 ,num):
        if num % x == 0:
            print(f"the number {num} is not a prime")
    else:
        print("it is a prime")
else:
    print("it is not a prime")
