# basic information 
name = ("      ONLINE GROCERY STORE","   FREE SHIPPING IN FEW HOURS","      GOOD QUALITY PRODUCT","       ORDER PLACE NOW")
for i in name :
    print(i)
x = (" ","    MENU   ")
for i in x :
    print(i)
# catagor which is available 
print("  CATAGORY  ")
catag = ["drink","snacks"]
for i in catag :
    print(i)
# dictionary which hold catagory of items 
product = {
    "drink":
    {
        "cold drink":["coca cola price 180","7up price 120","pepsi price 150"],
        "juice":["mango juice price 80pkr","apple juice price 70 pkr"],
        "water":["aqua fina price 30pkr ","nestle price 50pkr","dasani price 40 pkr"]
    },
    "snacks":
    {
        "chips":["lays price 20 pkr","kurkure price 25pkr","pringels price 160pkr"],
        "cakes":["cup cake price 10 pkr","fruit cake price 35 pkr"]
    }
}
# use function and if else condition to compare and return their price with quantity
def pro_name(item,quantity):
    if catagory in catag:
        if pro == "cold drink":
            if item == "coca cola":
                print(f"price of your product : {quantity*180}")
                return quantity*180
            elif item == "7up":
                print(f"price of your product : {quantity*120}")
                return quantity*120
            elif item == "pepsi":
                print(f"price of your product : {quantity*150}")
                return quantity*150
            else :
                return "this product is not available"
        elif pro == "juice":
            if item == "mango juice":
                print(f"price of your product : {quantity*80}")
                return quantity * 80
            elif item == "apple juice":
                print(f"price of this product : {quantity*70}")
                return quantity*70
            else:
                return "this product is not available"
        elif pro == "water":
            if item == "auqa fina":
                print(f"price of your product : {quantity*30}")
                return quantity*30
            elif item == "nestle":
                print(f"price of this product : {quantity*50}")
                return quantity*50
            elif item == "dasani":
                print(f"price of this product : {quantity*40}")
                return quantity * 40
            else:
                print("this product is not available")
                return 0
        elif pro == "chips":
            if item == "lays":
                print(f"price of your product : {quantity*20}")
                return quantity*20
            elif item == "kyrkure":
                print(f"price of this product : {quantity*25}")
                return quantity*25
            elif item == "pringles":
                print(f"price of this product : {quantity*160}")
            else:
                print("this product is not available")
                return 0
        elif pro == "cakes":
            if item == "cup cake":
                print(f"price of your product : {quantity*10}")
                return quantity*10
            elif item == "fruit cake":
                print(f"price of this product : {quantity*35}")
                return quantity*35
            else:
                print("this product is not available")
                return 0
    else :
        print("we dont have this catagory product ")
# use this variabe "total_bill" to store price of product 
total_bill = 0 
# use while loop with true func for continue shoping
while True:
    catagory = input("enter catagory : ")
    if catagory == "drink" :
        x = ["cold drink","juice","water"]
        for i in x:
            print(i)
    elif catagory == "snacks":
        y = ["chips","cakes"]
        for i in y :
            print(i)
    else :
        print("not available ")
    pro = input("enter product : ")
    x = product[catagory][pro]
    for i in x: 
        print(i)
    itm = input("enter product : ")
    quan = int(input("enter quantity : "))
    price = pro_name(itm,quan)
    total_bill+=price
    cont = input("if you want to continue type yes : ")
    if cont != "yes":
        break 
print(f"your total bill {total_bill}")
# customer information
print("enter your information")
cust_name = input("enter your name : ")
addres = input("enter your adress : ")
phone = input("enter phone number : ")
print("Thank you")
print("your order deliver in 3 hours")
