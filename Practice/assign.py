# from playsound import playsound
# playsound("C:\\Users\\acer\\Downloads\\creepy-halloween-bell-trap-melody-247720.mp3")


# a = "Hello"
# b = 45
# c = 23.43
# d = True
# e = None

# print(type(a))

# define username in list
#ask user for their username, if the username is in the list print login succesfull
#else login failed




user_data = {"rohan": "1234", "shyam": "12345"}

name = input("Enter your user name: ")
password = input("Enter your password: ")
try:
    if name in user_data :
        print("Login Successful!")
    else:
        print("Login Failed!")
except:
    print("Failed")