def decimal_to_binary(number):
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary
num = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(num)
print(f"Binary representation of {num} is {binary_representation}")
