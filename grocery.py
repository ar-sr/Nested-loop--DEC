
import os
def clear():
    os.system("clear")


grocery=[]



print("Welcome to grocery store inventory system, How can we help you:")


def addproduct():
    clear()
    product_name=input("please enter the product name:")
    product_quantity=int(input("please enter the quantity of the product:"))
    product_price=int(input("please enter the price of product:"))
    
    
    
    
    adpro={
        "name":product_name,
        "quantity":product_quantity,
        "price":product_price
    }
    
    
    
    grocery.append(adpro)
    print(f"product {product_name} added successfully!")







 
def displayproduct():
    for i in grocery:
        print("The Product Details Are.......")
        print(f"product_name:{i['name']}\n product_quantity:{i['quantity']} \n product_price:{i['price']}")
        
        
        
    

def searchproduct():
    searchkey=input("enter the name of the product you searching for:")
    
    
    
    
    for i in grocery:
        if i ['name'].lower()==searchkey.lower():
            print(f"product_name:{i['name']}\n product_quantity:{i['quantity']} \n product_price:{i['price']}")
            print("details fetched successfully!")

        else :
            print("Sorry The Item Not Found")
            
            
            

def updateproduct():
    update=input("enter the product name to be updated:")
    quan= int(input("enter the quantity to be updated" ))
    for i in grocery:
        if i['name'].lower()==update.lower():
            i['quantity']=quan
            print("updated succesfully!")
            print(f"product_name:{i['name']}\n product_quantity:{i['quantity']} \n product_price:{i['price']}")

    

        else:
            print("not found")







def removeproduct():
    search_name=input("Please Enter The Product Name You Want To Remove:")
    for i in grocery:
            if i['name'].lower()== search_name.lower():
                    grocery.remove(i)
                    print("product deleted as requested")
                    
            else :
                    print("error")
                
       







clear()


def main():
# main function starting:

    while True:
        print("tap 1 to add product")
        print("tap 2 to display product")
        print("tap 3 to search a product")
        print("tap 4 to update product quantity")
        print("tap 5 to remove product")
        print("tap 6 to exit")
    
    
    
    
    value=int(input("Tap The Number Here:"))
    
    
    
    
    if value==1:
        addproduct()  
    elif value==2:
        displayproduct()
    elif value==3:
        searchproduct()
    elif value==4:
        updateproduct()
    elif value==5:
        removeproduct()
    elif value==6:
        print("Have A Nice Day!")
        break
        
        
    else:
        print("Didn't Get You, Try Again Please")
        
        
    
if __name__=="__main__":
    main()