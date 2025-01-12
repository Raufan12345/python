#Args and kwargs
#args - takes multiple data, * is used to define args, data stored as tuple

# def student(*args):
#     for i in args:
#         print(i)

# fname = 'ram'
# student(fname,"shyam","gopal")


# craete a function that takes multiple numbers and print the sum of the numbers


def num(*args):
    a = 0
    for i in args:
        a += i
    return a
add = sum(1,43)
print(add)



#kawrgs - keyworded arguments, dictionary datatype, ** used to define kwargs

# def Student(age,**kwargs):
#     print(f"Age:{age}")
#     print(kwargs)

# Student(20,Name = "Ram",Name2 = "Shyam")