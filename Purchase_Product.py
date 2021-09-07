#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
print("__________________________________________Fill the details to Purchase Product_______________________________________")
f2 = open("sales.json",'r')
read2 = f2.read()
f2.close()
receipt = json.loads(read2)
choice='Y'
while(choice == 'Y' or choice == 'y' ):
    print("\nEnter :-\n\n> '1' to buy Product\n> '2' to display all Products Id and Name\n> '3' to display all purchase history\n> '4' to check quantity of a product\n")
    print("----------------------------------------------")
    inp = int(input())
    if inp == 1:
        f1 = open("record.json",'r')
        read = f1.read()
        f1.close()
        data = json.loads(read)
        p_id  = str(input("Enter the product Id: "))
        if data[p_id]['qn'] != 0:
            qnt = int(input("Enter the quantity: "))
            if data[p_id]['qn'] >= qnt:
                print("*************************************")
                print("Product ID: ", p_id)
                print("Product Name: ", data[p_id]['name'])
                print("Product Price: ", data[p_id]['pr'])
                print("Total Amount: ", data[p_id]['pr'] * qnt)
                print("*************************************")
                data[p_id]['qn'] = data[p_id]['qn'] - qnt
                sale_id=int(list(receipt.keys())[-1])
                receipt[sale_id+1] = {'prod' : p_id, 'qn' : qnt, 'amount': data[p_id]['pr'] * qnt}
                data2 = json.dumps(receipt)
                f2 = open("sales.json",'w')
                f2.write(data2)
                f2.close()
                data = json.dumps(data)
                f1 = open("record.json",'w')
                f1.write(data)
                f1.close()
            else:
                print("!!! Purchasing quantity is more than available quantity !!!\n")
        else:
            print("!!! No available Quantity !!!\n")
    elif inp == 2:
        f1 = open("record.json",'r')
        read = f1.read()
        f1.close()
        data = json.loads(read)
        for i in data:
            print(i," : ",data[i]['name'])
    elif inp == 3:
        print(json.dumps(receipt, indent=1))
    elif inp == 4:
        f1 = open("record.json",'r')
        read = f1.read()
        f1.close()
        data = json.loads(read)
        p_id = str(input("Enter product id: "))
        print(data[p_id]['qn'])
    choice = str(input("Do you wants to perform other operations? type: 'Y' for Yes\n"))
print("--------------------- Thanks for Visiting! ---------------------")


# In[ ]:




