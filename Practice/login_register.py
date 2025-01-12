import json

def register():
    username = input("Enter your uesrname:")
    password = input("Enter password:")

    user = {username:password}
    json_user = json.dumps(user)
    f = open('C:/Users/acer/Documents/Python/Practice/userdata.txt','a')
    f.write(json_user+'-')
    f.close()

def login():
    username = input("Enter your uesrname:")
    password = input("Enter password:")
    f = open('C:/Users/acer/Documents/Python/Practice/userdata.txt','r')
    data = f.read()
    f.close()
    print(data)
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            if dict_data.get(username) == password:
                print("login succesfull")



a = input("Register or login:").lower()
if a == "register":
    register()
elif a == "login":
    login()


