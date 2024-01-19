# class Vehicle():
#     def __init__(self,speed,milage):
#         self.speed = speed
#         self.milage = milage
        
# # Info_vehicle = Vehicle(140,20)
# # print("Vehicle speed is : ",Info_vehicle.speed)
# # print("Vehicle milage is : ",Info_vehicle.milage)


# class Bus(Vehicle):
#     pass

# school_bus = Bus(200,18)
# print("school bus speed : ",school_bus.speed)
# print("school bus milage : ",school_bus.milage)


class Square:
    def __init__(self,number):
        self.number = number
    def NumSquare(self):
        return self.number ** 2
    
squr = Square(5)
print(squr.NumSquare())
