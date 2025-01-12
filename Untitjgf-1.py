# # Name = input("Enter your name :")
# # Age = input("Enter your age :")
# # print("your name is" , Name, "! "+ Age )
# # print("your name is {} ".format(Name,Age) )
# # print(f"your name is {Name} and you are {Age} years old" )
# # Number = int(input("Enter your number:")) 


# #to check a value in a sequencial datatype
# #output in boolean datatype
# #in operation - true if output exist false elsewise
# #not in operation - true if output doesnt exist false elsewise


# fruit = "mango"
# fruit2 = "banana"
# Fruits = ["apple","mango"]
# print(fruit2 in Fruits)

# # is operation
# # is not operation  
# a = 34
# b = 43
# c = 34
# print(a is b)
# print(a is not b)
# print(a is c,c is not a)
# print(id(a))
# print(id(b))


# # conditional statements
# # if _else statement - multi lined statement
# #synatx:
# # if condition:
# #     statement
# # elif condition: ( if _else condition can have multiple elif )
# #     statement
# # else:
# #     statement


# a = 5
# b = 9

# if a > b:
#     print("a is greatre than b")

# elif a == b :
#     print("they are equal")
# else:
#     print("b is grester")  

# a=[1,2,3]
# b=[1,2,3,[1,2,3]]

# print(b in a)

# a = int(input("Enter your number:"))
# b = int(input("Enter your number:"))

# if a > b :
#     print(a is greater)

# elif a==b :
#     print("numbers are equal")

# elif a < b :
#     print("b is greater")


#requirements
#double number form user
#user bata euta operation (+,-,*,/)
#if user operation + performs addition and print output and likewise



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


















#mark evaluation
#Requirements
#exam mark for users


# print("Enter your Marks")
# score = int(input())

# if score >= 90 and score <= 100:
#     print("Excellent")
# elif score >= 80 and score <= 90:
#     print("Very Good")
# elif score >= 70 and score <= 80:
#     print("Good")
# elif score >= 60 and score <= 70:
#     print("Better")
# elif score >= 50 and score <= 60:
#     print("Could be better")
# elif score >= 40 and score <= 50:
#     print("Pass")
# elif score < 40:
#     print("Fail")
# else:
#     print("404")