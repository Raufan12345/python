# import array as ar

# a = ar.array("u",["1","2","3","4"])
# print(a)


# function - like a variable it stores block of code insteas of data
#def - used to define function
# def fn_name():
#     print("hmnnsd")
#     print("hmnnsd")
#     print("hmnnsd")

# fn_name()
#positional argument - first parameter takes first argument value
# variable defined in the parameter are called arguments

# def name(firstname,lastname,died,age = 50 ):# default argument - example age (mentioned within the function)
#     print(firstname)
#     print(lastname)
#     print(died)
#     print(age)

# fname = "bishal"
# lname = "mukhiya"
# name(fname,lname,2024)

#keyword argument:

# def name(firstname,lastname,age):
#     print(firstname)
#     print(lastname)
#     print(age)
# lname = "Mukhiya"
# fname = "Bishal"
# fname1 = "ram"
# lname1 = "hari"

# name(firstname = fname,age = 20, lastname = lname )
# name(firstname = fname1,age = 29, lastname = lname1 )

# local value = value defined inside the function
# global value = value defined outside the function
# golbal value can be used inside local function whereas local value cannot be used outside function

# def user_info(firstname, lastname, age,born = "Born - 2000" ):
#     print(firstname)
#     print(lastname)
#     print(age)
#     print(born)
# fname = "Name - Ram"
# lname = "Lname - Kumar"
# user_info(firstname = fname, lastname = lname, age = "Age - 20" )