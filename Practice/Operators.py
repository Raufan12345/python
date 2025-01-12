# a = int(input("num1: \n"))
# b = int(input("num\2: \n"))

# squ = (a + b)* (a + b)
# print("the squ is:", squ)

# a = ("Satish")

# print(a)

y = "y"
while y == "y":
    try:
        a = int(input("Enter your 1st number: "))
        b = int(input("Enter your 2nd number: "))
        ope = input("Enter your operation: ")

        if ope == "+":
            print(a + b)

        elif ope == "-":
            print(a - b)

        elif ope == "*":
            print(a * b)

        elif ope == "/":
            print(a / b)
        else:
            print("Invalid number")
    except:
        print("invalid")



