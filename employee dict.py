employee_data={
    "employee1":{
        "name":"alice",
        "age":28,
        "position":"software engineer"        
    },
    "employee2":{
        "name":"bob",
        "age":35,
        "position":"data scientist"
    },
    "employee3":{
        "name":"charlie",
        "age":"42",
        "position":"product manager"
    }

}


name=input("enter ur name:")
age=int(input("enter your age"))
position =input("enter your position")

newdata={
    "name":name,
    "age":age,
    "position":position
    
    
}



employee_data["employee4"]=newdata
print(employee_data)