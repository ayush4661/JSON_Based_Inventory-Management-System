import json
print("_________________________________________Inventory Management System__________________________________________")
f1 = open("record.json",'r')
read = f1.read()
f1.close()
data = json.loads(read)
choice='Y'
while(choice == 'Y' or choice == 'y' ):
    print("\n---------------------------------------------")
    print("\nEnter :- \n\n> '1' to display available Products\n> '2' to display all Products Id and Name\n> '3' for adding Product\n> '4' to delete Product\n> '5' to find Product details by Product ID\n> '6' to check quantity of a product\n> '7' to update quantity of a product")
    print("\n---------------------------------------------")
    inp=int(input())
    if inp == 1:
        print(json.dumps(data, indent=1))
    elif inp == 2:
        for i in data:
            print(i," : ",data[i]['name'])
    elif inp == 3:
        p_id = str(input("Enter product id: "))
        name = str(input("Enter Product name: "))
        pr = int(input("Enter Product price: "))
        qn = int(input("Enter quantity: "))
        data[p_id] = {'name': name, 'pr': pr, 'qn': qn}
    elif inp == 4:
        del data[str(input("Enter Product ID: "))]
        print("----- Product Deleted Successfull! -----")
    elif inp == 5:
        print(data[(input("Enter Product ID: "))])
    elif inp == 6:
        p_id = str(input("Enter product id: "))
        print(data[p_id]['qn'])
    elif inp == 7:
        p_id = str(input("Enter product id: "))
        qn = int(input("Enter quantity to add: "))
        data[p_id]['qn'] = str(int(data[p_id]['qn'])+qn)
        print("----- Updation Successfull! -----")
    choice = str(input("Do you wants to perform other operations? type: 'Y' for Yes\n"))
data = json.dumps(data)
f1 = open("record.json",'w')
f1.write(data)
f1.close()
