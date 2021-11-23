from app import db, Orders, Products, Product_order 

db.create_all()

ps4 = Products(name= 'Playstation 4',
                order= 1 )

wii = Products(name= 'Wii',
                order= 2 )

order1 = Orders(order= 1,
)
order2 = Orders(order= 2)

db.session.add(ps4)
db.session.add(wii)
db.session.add(order1)
db.session.add(order2)
db.session.commit()

print(f"The ps4 is in: {ps4.order[0].order}, {ps4.order[1].order}")


