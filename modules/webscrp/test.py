from graphene import ObjectType, String, Field, Schema, Int, Float
import graphene
from graphql import GraphQLError

# Importing the library
import psutil
import time

start = time.time()

def show(value_d):
    final_result = float(value_d) * 4.5
    # Getting % usage of virtual_memory ( 3rd field)
    print('RAM memory % used:', psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
    print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
    print('2',final_result)
    return final_result

class TestOne(ObjectType):
    value_d = Float(required=True)
    print('1--------------',value_d)

class MyTestOne(graphene.ObjectType): 
    testone = Field(TestOne, value_d=Int())

    def resolve_testone(self, info, value_d):
        result = show(value_d)
        return TestOne(value_d=result)

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")