from app import db, Customers, Products, Orders

db.create_all()

customers = [""]

option = input("Add another user?")

if option == "yes" or "Yes":
    name= input("Customer name: ")
    customers.append(name)

elif option == "no" or "No":
    for i in customers:
        new = Customers(name=i)
    return Customers.name.query.all()



customer1 = Customers(name= "Sunmola")

customer2 = Customers(name= "Yoan")

customer3= Custoe