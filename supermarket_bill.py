from datetime import datetime
Name=input("Enter your Name:")
products='''
Rice     Rs 20/Kg
sugar    Rs 40/Kg
salt     Rs 12/kg
oil      Rs 140/L
panner   Rs 150/Kg
maggie   Rs 80/kg
milk     RS 60/L
curd     Rs 80/Kg
Colgate  Rs 110/250G
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#Cost Per items
items={'rice':20,
       'sugar':40,
       'salt':12,
       'oil':140,
       'panner':150,
       'maggie':80,
       'milk':60,
       'curd':80,
       'colgate':110}
choice=int(input('''Enter 1 For Items or 2 for Exit'''))
if choice==1:
    print(products)
for i in range(len(items)):
    C=int(input('''Enter 1 press to buy or 2 to Exit'''))
    if C==2:
        break
    if C==1:
        item=input("Enter  your Item")
        quantity=int(input("Enter Quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            Gst=(totalprice*5)/100
            finalprice=Gst+totalprice
        else:
            print("Entered Item Is Not Available")
    else:
        print("Enter correct Number for Items")
    Bill=input("Can i Bill your Items Yes or No")
    if Bill=='yes':
        pass
        if finalprice!=0:
            print(25*"=","Dmart",25*"=")
            print(22*"=","Miryalaguda",25*"=")
            print("Name:",Name,30*"","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',8*" ",'price')            
            for i in range(len(pricelist)):
                print(i,5*' ',10*' ',ilist[i],8*' ',qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*"-",'TotalAmount:','Rs',totalprice)
            print(50*"-",'GST AMOUNT:','Rs',Gst)
            print(75*"-")
            print(50*"-",'FinalAmount:','Rs',finalprice)
            print(75*"-")
            print(50*"-","Thanking You For Visit")
            