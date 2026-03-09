from pydantic import BaseModel

class Demo(BaseModel):
    name:str
    age:int

def function1(pydantic: Demo):
    print("Funtion 1")
    print(pydantic.name)
    print(pydantic.age)

def function2(pydantic: Demo):
    print("Function 2")
    print(pydantic.name)
    print(pydantic.age)
    print(type(pydantic.age))

data = {'name':"Sakshi",'age':22}

object = Demo(**data)

# Calling function 1 and function 2 by passing pydantic object
function1(object)
function2(object)

# If we pass wrong type of data pydantic raise error
# data1 = {'name':"Sakshi",'age':"Twenty-two"}
# object2 = Demo(**data1)
# function1(object2)
# function2(object2)

# Pydantic automatically converts types wherever required
data1 = {'name':"Sakshi",'age':'22'}
object2 = Demo(**data1)
function1(object2)
function2(object2)