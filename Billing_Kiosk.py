    #CREATING PYTHON MYSQL INTERFACE

import mysql.connector
mypass=input("Enter the password: ") #ASKING PASSWORD TO ACCESS DATABASE

if mypass!="t2a3N1a1y$":
    print("Wrong password")

else:
    

    mycon=mysql.connector.connect(host="localhost",user="root",passwd=mypass,charset="utf8")

        
    cursor=mycon.cursor()
    cursor.execute("create database if not exists project;")
    cursor.execute("use project;")
    cursor.execute("create table if not exists stock_details (item_name varchar(25),price int,qty int);")


    cursor.execute("select * from stock_details;") #RETRIEVING DATA FROM TABLE IF ALREADY EXISTS
    data=cursor.fetchall()
    dict_products={}

    for i in data:
        dict_products[i[0]]=[i[2],i[1]]

    

    bill={}
    bill_total=0

    def finalprice(product): #FUNCTION TO OBTAIN FINAL AMOUNT FOR BILL 

        global cost,GST

        cost=round(dict_products[product][1]*qty,2)

        GST=round(cost*0.09,2)

        total=round(cost+GST,2)
        return total


    while True: #MAIN LOOP TO RE-RUN ENTIRE PROOGRAM
        print()
        print()
        print('''              

    Given below is the list of options available in the program,

                          OPTIONS 
                       *~~~~~~~~~~~*
                       1)View existing stock details
                       2)Generate bill
                       3)Add Stock
                       4)Reduce Stock
                       5)Update price of items
                       6)Add new products
                       7)Delete record
                       8)Exit
                                                       Made by: Tanay Shah''')
         


        print()
        input_option=int(input('Enter the  option number you would like to go with: '))   #OPTIONS FOR USER
        print()

        #OPTION 1 STARTS HERE, OPTION 1 =>> JUST SHOWS STOCK DETAILS
        if input_option==1:

            if len(dict_products)>0:
                print("List of the items available is given below along with their quantity and price")
                print()

                print("*"+"-"*52+"*")
                print("| Item                       | Price(Rs) | Qty       |")
                print("|"+"-"*52+"|")


                for items in dict_products:
                    print("|",items," "*(25-len(items)),"|",
                 dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                          "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                print("*"+"-"*52+"*")
                print()
                print("The price mentioned is for per unit/box/pack of the item")
                print()
            else:
                print("List of the items available is given below along with their quantity and price")
                print()

                print("*"+"-"*52+"*")
                print("| Item                       | Price(Rs) | Qty       |")
                print("|"+"-"*52+"|")


                for items in dict_products:
                    print("|",items," "*(25-len(items)),"|",
                 dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                          "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                print("*"+"-"*52+"*")
                print()
                print("The price mentioned is for per unit/box/pack of the item")
                print("No item currently available in stock")
                print()

        #OPTION 2 STARTS HERE OPTION 2 =>> GENERATE BILL

        if input_option==2:
            if len(dict_products)==0:
                print("No item in stock,bill cannot be generated")
                print()
            else:

                while True:
                    print("List of the items available is given below along with their quantity and price")
                    print()

                    print("*"+"-"*52+"*")
                    print("| Item                       | Price(Rs) | Qty       |")
                    print("|"+"-"*52+"|")


                    for items in dict_products:
                        print("|",items," "*(25-len(items)),"|",
                     dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                              "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                    print("*"+"-"*52+"*")
                    print()
                    print("The price mentioned is for per unit/box/pack of the item")
                    print()
                    no_of_products=int(input('Enter  the total number of items to be billed: '))
                    print()


                    for i in range(no_of_products):
                        product=input('Enter the item to be billed: ').lower()
                    
                        if product in dict_products:
                            qty=int(input('Enter the quantity of the item: '))     
                            print()
                            if qty>dict_products[product][0]:
                                print("Insufficient stock")
                                print()
                            else:

                                sum1=finalprice(product)

                                dict_products[product][0]-=qty

                                cursor.execute("update stock_details set qty="+str(dict_products[product][0])+" where item_name='"+product+"';")

                                cursor.execute("commit;") #UPDATING STOCK IN THE  SQL TABLE

                                bill_total+=sum1

                                bill[product]=[qty,GST,sum1]
                        else:
                         print('Item not available')
                         print()

                    if len(bill)==0:     
                        print("No item entered in the bill ")
                        print()
                    else:
                            
                        ask5=input('''Do you want to apply  any discount? 
    Enter yes/no: ''').lower()
                        print()

                        if ask5=="yes":
                            discount=float(input("Enter the discount to be applied( in %): "))
                            print()

                            if discount>100:
                                print("Discount cannot be above 100%")
                                print()
                            else:    
                                discounted_price=round(bill_total-(bill_total*discount)/100,2)
                                print()
                                                                
                                print("*"+"-"*79+"*")            
                                print("|"," "*26,"**********************"," "*27,"|")
                                print("|"," "*25,"**********Bill**********"," "*26,"|")
                                print("|"," "*26,"**********************"," "*27,"|")
                                print("| Retail Invoice for Prakash Stationers"," "*39,"|")
                                print("| GSTIN 24AAECR2971C1Z5"," "*30,"Phone: 079-27345869"," "*4,"|")
                                print("*"+"-"*79+"*")
                                print("| Item                       | Cost(1U) | Qty        | GST        | Final price |")
                                print("*"+"-"*79+"*")


                                for product in bill:
                                    print("|",product," "*(25-len(product)),"|",dict_products[product][1],
                                      " "*(7-len(str(dict_products[product][1]))),"|",bill[product][0],
                                      " "*(9-len(str(bill[product][0]))),"|",bill[product][1],
                                      " "*(9-len(str(bill[product][1]))),"|",bill[product][2],
                                    " "*(10-len(str(bill[product][2]))),"|")

                                print("|"+"-"*79+"|")
                                print("|"," "*47,"Discount applied:",discount,"%"," "*(8-len(str(discount))),"|")
                                print("|"+"-"*79+"|")
                                print("|"," "*47,"Total amount(Rs):",round(discounted_price,2)
                                      ," "*(10-len(str(discounted_price))),"|")
                                print("*"+"-"*79+"*")
                                bill.clear()                                                                                      
                                bill_total=0

                        if ask5=="no":

                            print("*"+"-"*79+"*")            
                            print("|"," "*26,"**********************"," "*27,"|")
                            print("|"," "*25,"**********Bill**********"," "*26,"|")
                            print("|"," "*26,"**********************"," "*27,"|")
                            print("| Retail Invoice for Prakash Stationers"," "*39,"|")
                            print("| GSTIN 24AAECR2971C1Z5"," "*30,"Phone: 079-27345869"," "*4,"|")
                            print("*"+"-"*79+"*")
                            print("| Item                       | Cost(1U) | Qty        | GST        | Final price |")
                            print("|"+"-"*79+"|")


                            for product in bill:
                                print("|",product," "*(25-len(product)),"|",dict_products[product][1],
                                  " "*(7-len(str(dict_products[product][1]))),"|",bill[product][0],
                                  " "*(9-len(str(bill[product][0]))),"|",bill[product][1],
                                  " "*(9-len(str(bill[product][1]))),"|",bill[product][2],
                                " "*(10-len(str(bill[product][2]))),"|")

                            print("|"+"-"*79+"|")
                            print("|"," "*46,"Discount applied : None"," "*6,"|")
                            print("|"+"-"*79+"|")
                            print("|"," "*47,"Total amount(Rs):",round(bill_total,2),
                                  " "*(10-len(str(bill_total))),"|")
                            print("*"+"-"*79+"*")

                            bill.clear()                                                                                      
                            bill_total=0

                    ask2=input('''Do you want to generate another bill?
    Enter yes/no: ''').lower()
                    print()

                    if ask2=="yes":
                        continue
                    if ask2=="no":
                        break
                  
        #OPTION 3 STARTS HERE, OPTION 3 =>> ADD STOCK

        elif input_option==3:

            while True:

                print("Current stock of the items is as follows")
                print("*"+"-"*40+"*")
                print("| Item                       | Qty       |")
                print("|"+"-"*40+"|")


                for stock_curr in dict_products:
                    print("|",stock_curr," "*(25-len(stock_curr)),"|",
                 dict_products[stock_curr][0]," "*(8-len(str(dict_products[stock_curr][0]))),"|")
                print("*"+"-"*40+"*")
                print()


                no_of_prod1=int(input("Enter the number of items whose stock is to be increased: "))
                print()


                for add in range(no_of_prod1):
                    prodstk_add=input("Which item's stock do you want to add? ").lower()

                    if prodstk_add in dict_products:
                        qty_add=int(input("How much stock do you want to increase? "))
                        print()
                        dict_products[prodstk_add][0]+=qty_add
                        cursor.execute("update stock_details set qty="+str(dict_products[prodstk_add][0])+" where item_name='"+prodstk_add+"';")
                        cursor.execute("commit;")
                    else:
                        print("Item not available")
                        print()

                print('''Stock successfully updated
    Updated list of items is''') 
                print("*"+"-"*40+"*")
                print("| Item                       | Qty       |")
                print("|"+"-"*40+"|")
                for stock_add in dict_products:
                    print("|",stock_add," "*(25-len(stock_add)),"|",
                 dict_products[stock_add][0]," "*(8-len(str(dict_products[stock_add][0]))),"|")
                print("*"+"-"*40+"*")
                print()    

                ask6=input('''Do you want add stock of any other item?
    Enter yes/no: ''').lower()
                print()
                if ask6=="yes":
                    continue
                if ask6=="no":
                    break
                    


        #OPTION 4 STARTS HERE, OPTION 4 =>>REDUCE STOCK

        elif input_option==4:

            while True:

                print("Current stock of the items is as follows")
                print("*"+"-"*40+"*")
                print("| Item                       | Qty       |")
                print("|"+"-"*40+"|")

                for stock_cur in dict_products:
                    print("|",stock_cur," "*(25-len(stock_cur)),"|",
                 dict_products[stock_cur][0]," "*(8-len(str(dict_products[stock_cur][0]))),"|")
                print("*"+"-"*40+"*")
                print()
                no_of_prod2=int(input("Enter the number of items whose stock is to be reduced: "))
                print()

                for reduce in range(no_of_prod2):
                    prodstk_reduce=input("Which item's stock do you want to reduce? ").lower()

                    if prodstk_reduce in dict_products:
                        qty_reduce=int(input("How much stock do you  want to reduce? "))
                        print()

                        if qty_reduce>dict_products[prodstk_reduce][0]:
                            print("Quantity of the item cannot be below zero")
                            print()
                        else:                                                     
                            dict_products[prodstk_reduce][0]-=qty_reduce
                            cursor.execute("update stock_details set qty="+str(dict_products[prodstk_reduce][0])+" where item_name='"+prodstk_reduce+"';")
                            cursor.execute("commit;")

                    else:
                        print("Item not available")
                        print()
                print('''Stock successfully updated
    Updated list of items is''')
                print()
                print("*"+"-"*40+"*")
                print("| Item                       | Qty       |")
                print("|"+"-"*40+"|")

                for stock_reduce in dict_products:
                    print("|",stock_reduce," "*(25-len(stock_reduce)),"|",
                     dict_products[stock_reduce][0]," "*(8-len(str(dict_products[stock_reduce][0]))),"|")
                print("*"+"-"*40+"*")
                print()    
                                         
                ask7=input('''Do you want reduce stock of any other item?
    Enter yes/no: ''').lower()
                print()
                if ask7=="yes":
                    continue
                if ask7=="no":
                    break

        #OPTION 5 STARTS HERE, OPTION 5 =>> UPATING PRIICE

        elif input_option==5:
            while True:
                print("Details of items with their current price is as follows")
                print("*"+"-"*40+"*")
                print("| Item                       | Price(Rs) |")
                print("|"+"-"*40+"|")


                for price in dict_products:
                    print("|",price," "*(25-len(price)),"|",
                     dict_products[price][1]," "*(8-len(str(dict_products[price][1]))),"|")
                print("*"+"-"*40+"*")
                print()
                print("The price mentioned is for per unit/box/pack of the item")
                print()

                no_of_prod3=int(input("Enter the number of items whose price is to be updated: "))

                for price in range(no_of_prod3):
                    product_prcupdt=input("Enter the item whose price is to be updated: ")

                    if product_prcupdt in dict_products: 
                        newprice=int(input("Enter the new price: "))
                        print()

                        if newprice<0:
                            print("Price cannot be negative")                                
                            print()
                        else:
                            dict_products[product_prcupdt][1]=newprice
                            cursor.execute("update stock_details set price="+str(dict_products[product_prcupdt][0])+" where item_name='"+product_prcupdt+"';")
                            cursor.execute("commit;")                   
                    else:
                        print("Item not available")
                        print()

                print('''Prices successfully updated 
    Updated list of prices is''')
                print("*"+"-"*40+"*")
                print("| Item                       | Price(Rs) |")
                print("|"+"-"*40+"|")
                for price in dict_products:
                    print("|",price," "*(25-len(price)),"|",
                     dict_products[price][1]," "*(8-len(str(dict_products[price][1]))),"|")
                print("*"+"-"*40+"*")
                print()
                print("The price mentioned is for per unit/box/pack of the item")
                print()
                              
                ask3=input('''Do you want to make anymore changes?
    Enter yes/no: ''').lower()
                print()
                if ask3=="yes":
                    continue
                if ask3=="no":
                    break

        #OPTION 6 STARTS HERE, OPTION 6 =>> ADD NEW PRODUCTS

        elif input_option==6:
            while True:
                print("List of the items available is given below along with their quantity and price")
                print()

                print("*"+"-"*52+"*")
                print("| Item                       | Price(Rs) | Qty       |")
                print("|"+"-"*52+"|")


                for items in dict_products:
                    print("|",items," "*(25-len(items)),"|",
                 dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                          "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                print("*"+"-"*52+"*")
                print()
                no_new_prod=int(input("How many new items do you want to enter? "))
                print()


                for new_prod in range(no_new_prod):
                    add_prod=input("Enter the new item: ").lower()
                    
                    if add_prod in dict_products:
                        print("Item already available")
                        print()
                    else:
                        price=int(input("Enter the price of the new item: "))
                        
                        qty_newprod=int(input("Enter the quantity of the new item: "))
                        print()
                        dict_products[add_prod]=[qty_newprod,price]
                        cursor.execute("insert into stock_details values('"+add_prod+"',"+str(price)+","+str(qty_newprod)+");") 
                        cursor.execute("commit;")
                        
                print('''New items have successfully been added!

     Updated list of items is as follows:''')
                print("*"+"-"*52+"*")
                print("| Item                       | Price(Rs) | Qty       |")
                print("|"+"-"*52+"|")
                for items in dict_products:
                    print("|",items," "*(25-len(items)),"|",
                 dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                          "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                print("*"+"-"*52+"*")
                print()
                print("The price mentioned is for per unit/box/pack of the item")
                print()


                ask4=input('''Do you want to add anymore items?
    Enter yes/no: ''').lower()
                print()
                if ask4=="yes":
                    continue
                if ask4=="no":
                    break

        #OPTION 7 STARTS  HERE, OPTION 7 =>> DELETE RECORDS

        



        elif input_option==7:

            while True:
                option=int(input('''Press 1 to delete the details of a specific item,
    Press 2 to delete all the details (details include item, its quantity and price): '''))
                print()

                if option==1:
                    print("List of the items available is given below along with their quantity and price")
                    print()
                    print("*"+"-"*52+"*")
                    print("| Item                       | Price(Rs) | Qty       |")
                    print("|"+"-"*52+"|")

                    for items in dict_products:
                        print("|",items," "*(25-len(items)),"|",
                     dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                              "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                    print("*"+"-"*52+"*")
                    print()

                    num=int(input("Enter the number of items whose data is to be deleted: "))
                    print()              

                    for delete in range(num):
                        prod_delete=input("Enter the item whose data is to be deleted: ").lower()
                        print()

                        if prod_delete in dict_products: 
                            dict_products.pop(prod_delete)
                            cursor.execute("delete from stock_details where item_name='"+prod_delete+"';")
                            cursor.execute("commit;")
                        else:
                            print("Item not available")
                            print()
                    print('''Record successfully deleted!
    Updated list of items is''')
                    print()

                    print("*"+"-"*52+"*")
                    print("| Item                       | Price(Rs) | Qty       |")
                    print("|"+"-"*52+"|")

                    for items in dict_products:
                        print("|",items," "*(25-len(items)),"|",
                     dict_products[items][1]," "*(8-len(str(dict_products[items][1]))),
                              "|",dict_products[items][0]," "*(8-len(str(dict_products[items][0]))),"|")
                    print("*"+"-"*52+"*")
                    print()
                    
                elif option==2:
                    ask8=input('''Are you sure you want to delete all the record?
    The existing record will be deleted and you will have enter fresh data to do any other activity!
    Enter yes/no to proceed: ''').lower()
                    print()
                    if ask8=="yes":
                        dict_products.clear()
                        cursor.execute("delete from stock_details;")
                        cursor.execute("commit;")
                        print("All the records have been successfully deleted")
                        print()
                    if ask8=="no":
                        print("Your existing record is intact :) ")
                    
                ask9=input('''Do you want to make any other changes?
    Enter yes/no: ''').lower()
                print()
                if ask9=="yes":
                    continue
                if ask9=="no":
                    break

            ask1=input('''Do you want to run the program again?
        Enter yes/no: ''').lower()
            print()
            if ask1=="yes":
                continue
            if ask1=="no":
                break

        elif input_option==8: #option 8 to end the program
            break
