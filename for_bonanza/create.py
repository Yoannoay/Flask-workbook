from app import db, Customers

db.create_all()

customers = []

# option = input("Add another user?")
# bug "if option" doesnt care what i put in it still asks for customer name?



def c_name():
    option = input("Add another user?")
    if option.lower() == "yes":
        name= input("Customer name: ")
        customers.append(name)
        
        return customers
    else:
        return customers
    
    
# stopage = int(len(customers))
# # stop_2 = int(stop)
# print(stopage)
# print(customers)

def classing():
    for i in customers:
        new = Customers(name=i)
        db.session.add(new)
        db.session.commit()
    names = []
    all_c = Customers.query.all()
    for customer in all_c:
        names.append(customer.name)
    return f"Current customer entries: {names}"



# def printer():
#     for name in customers:
#         print(Customers.name.all())

    
    
c_name()
print(classing())
# printer()
# print(customers)