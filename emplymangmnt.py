

employee=[]


def addemployee():
    name=input("enter your name:")
    age=int(input("enter your age:"))
    job=input("enter your job:")
    
    
    
    emp = {
        "name":name,
        'age':age,
        'job':job
    }


    employee.append(emp)
    print(f"employee  {name} added successfully")


def displayemp():
    for i in employee:
        print("the employee deatils are.......")
        print (f"name: {i['name']} \n age: {i['age']} \n job: {i['job']}")
        
        
        
        
def searchemp():
    searchkey=input("enter the user name:")
    
    
    for i in employee:
        if i['name'].lower()==searchkey.lower():
            print("details fetched successfully")
            print(f"name: {i['name']}, age :{i['age']} job :{i['job']}")
        else:
            print("not found")
            



def delemp():
    search_name=input("enter user name to delete")
    for i in employee:
        if i['name'].lower()==search_name.lower():
            employee.remove(i)
            print("deleted")
        else:
            print("not found")








while True:
    print("enter 1 to add employee details:")
    print("enter 2 to add display employee details:")
    print("enter 3 to add search employee details:")
    print("enter 4 to add delete employee details:")
    
    
    
    value=input("enter the key here:")
    
    
    
    
    if value=="1":
        addemployee()
    elif value=="2":
        displayemp()
    elif value=="3":
        searchemp()
    elif value=="4":
        delemp()
    elif value=="5":
        print("have a nice day")
        break
    
    
    
    else:
        print("you have entered wrong input pls try again")