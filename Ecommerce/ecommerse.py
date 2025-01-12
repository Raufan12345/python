# Requirements:
# ask user for login or register
# if register ask for their username, password and usertype(buyer/ seller),(format for data store may change) and store it in a file
# if login ask for their username, password and check if it exist in the file, if it exist print some message.
# if user is buyer then, show them the option to view products and to buy products and view bill, if the choice is view product then show them the details of the products
# if user is seller then, show them the option to add products and view products, if the choice is add products then they have to enter the name, description, price of the product
import json

def view_your_product(seller):
   f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','r')
   data = f.read().split('-')
   f.close()
   for i in data:
      if i != '':
         dict_data = json.loads(i)
         if dict_data.get('seller') == seller:
            print(dict_data)

def buy_product():
   f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','r')
   data = f.read().split('-')
   f.close()
   for i in data:
      if i != '':
         dict_data = json.loads(i)
         print(dict_data)
   buy = input("What do you want to buy?>> ")
   quantity = int(input("How many? >> "))
   for i in data:
      if i != '':
         dict_data = json.loads(i)
         if dict_data.get('name') == buy:
            total = int(dict_data.get('price')) * quantity
            print("Total price is: ", total)
   
def view_product():
   f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','r')
   data = f.read().split('-')
   f.close()
   for i in data:
      if i != '':
         dict_data = json.loads(i)
         print(dict_data)


def add_product(username):
   name = input("Enter the name of product:")
   description = input("Enter the descripotion of product:")
   price = input("Enter price of product:")
   
   data = {"name":name, "description":description, "price":price,"seller":username}
   f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','a')
   json_data = json.dumps(data)
   f.write(json_data + '-')
   f.close()


def register():
   username = input("Enter your username:")
   password = input("Enter password:")
   usertype = input("Enter usertype(buyer/seller):")
   if usertype not in ['buyer','seller']:
      print("Invalid usertype")
   else:
      user = {'username':username,'password':password, 'usertype':usertype}
      json_user = json.dumps(user) #convert dict into json format
      f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','a')
      f.write(json_user+'-')
      f.close()


def login():
   is_login = False
   username = input("Enter username: ")
   password = input("Enter password:")
   f = open('C:/Users/acer\Documents/Python/Ecommerce/product.txt','r')
   data = f.read().split("-")
   f.close()
   for i in data:
      if i != '':
         dict_data = json.loads(i)   # json format convert dict
         if dict_data['username'] == username and dict_data['password'] == password:
            is_login = True
            usertype = dict_data.get('usertype')
   
   if is_login:
      print("Login success")
      if usertype == 'buyer':
         inp = input('''1. View product
2. Buy products''')
         if inp == '1':
            view_product()
         elif inp == "2":
            buy_product()
         else:
            print("Invalid choise")
      
      
      elif usertype == 'seller':
         inp = input('''1. Add product
2. View your products''')
         if inp == '1':
            add_product(username)
         elif inp =='2':
            view_your_product(username)
         else:
            print("Invalid choise")
   else:
      print("Invalid")


a = input("Register or Login:").lower()
if a == "register": 
   register()
elif a == "login":
   login()
