import heapq
from collections import defaultdict, OrderedDict
# Basic driver entity that would encapsulate
# driver related information.

class Car:
    def __init__(self, registration_number_car, driver_age):
        self.registration_number_car = registration_number_car
        self.driver_age = driver_age

    def __str__(self):
        return "Car [registration_number_car=" + self.registration_number_car + ", Age=" + self.driver_age + "]"

# class Parking_Slot:
#     def __init__(self, slot_number) :
#         self.slot_number = slot_number

class Parking_Lot:
    def __init__(self, total_slots):
        self.registration_slot_mapping = dict()
        self.age_registration_mapping = defaultdict(list)
        # we need to maintain the orders of cars while showing 'status'
        self.slot_car_mapping = OrderedDict()
        self.car_number_registration_mapping = set()
        # initialize all slots as free
        self.available_parking_lots = []
        # Using min heap as this will always give minimun slot number in O(1) time
#       Using heap to store the slots,
#       Ideally should be using database for managing
#       real world cases
     
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)
#       Provides information based on whether
#      the given slot is open or closed
#      Default OPEN
     
    def status(self):
        for slot, car in self.slot_car_mapping.items():
            print("Slot no: {} {}".format(slot, car))

    def get_closest_slot(self):
        return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None

    def free_slot(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        if found:
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.age_registration_mapping[car_to_leave.driver_age].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print("Slot number "+format(slot_to_be_freed)+" vacated, the car with vehicle registration number "+format(found)+ " left the space, the driver of the car was of age "+format(car_to_leave.driver_age))
            return 1
        else:
            print("slot is not in use")
            return

    def park_car(self, car):
        slot_no = self.get_closest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return 0
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number_car] = slot_no
        # print("slot_no "+ str(slot_no))
        # slot_number = Parking_Slot(slot_no)
        self.car_number_registration_mapping.add(car.registration_number_car)
        self.age_registration_mapping[car.driver_age].append(car.registration_number_car)
        return 1

    # ● Registration numbers of all cars of a particular colour.
    def get_registration_nos_by_age(self, driver_age):
        # print(self.age_registration_mapping)
        return self.age_registration_mapping[driver_age]

    # ● Slot numbers of all slots where a car of a particular colour is parked.
    def get_slot_numbers_by_age(self, driver_age):
        # print("slot by age ", self.age_registration_mapping)   
        if self.age_registration_mapping[driver_age]: 
            return [self.registration_slot_mapping[reg_no] for reg_no in self.age_registration_mapping[driver_age]]
        else:
            print("No driver with the age " + driver_age + " parked the car")
            return
    
    # Slot number by registration number
    def get_slot_numbers_by_registration(self, registration_no):
        # print(self.car_number_registration_mapping)
        for key_number in self.car_number_registration_mapping:
            if key_number == registration_no:
                return [self.registration_slot_mapping[key_number]]
            
        print("The Car with registration Number not present")
        

if __name__ == "__main__":
    with open("sample.txt") as file:
        lines = [(line.strip()) for line in file]
#     Initiates the parking slots
# Number of initial parking slots available
    number_of_slots=int(lines[0].split(' ')[-1])
    number_of_actions=len(lines)-1
    print("Created parking of "+format(number_of_slots)+" slots")
    
    parking_lot = Parking_Lot(number_of_slots)
    for i in range(1,number_of_actions+1):
        action_command=lines[i]
        action_key=action_command.split(' ')[0]
# Assigns a slot number to the driver
# We can add more constraints here as to how
# we would want to select assignable slots
        if action_key=="Park":
            registration_no=action_command.split(' ')[1]
            driver_age=action_command.split(' ')[-1]
            car = Car(registration_no, driver_age)
            return_flag = parking_lot.park_car(car)
#             slot_nos is the slot number
            slot_nos = parking_lot.get_slot_numbers_by_age(driver_age)
            if return_flag != 0:
                print("Car with vehicle registration number "+format(registration_no)+" has been parked at slot number "+format(slot_nos[-1]))

        elif action_key=="Slot_numbers_for_driver_of_age":
            driver_age=action_command.split(' ')[-1]
            # print("driver age : "+driver_age)
            slot_nos = parking_lot.get_slot_numbers_by_age(driver_age)
            if slot_nos:
                print(format(slot_nos))
         

        elif action_key=="Slot_number_for_car_with_number":
            registration_no=action_command.split(' ')[-1]
            # print("registration no: ", registration_no)
            slot_nos = parking_lot.get_slot_numbers_by_registration(registration_no)
            if slot_nos:
                print(slot_nos)

        elif action_key=="Leave":
            count=int(action_command.split(' ')[-1])
            slot_no_to_be_freed = count
            parking_lot.free_slot(slot_no_to_be_freed)
            heapq.heappush(parking_lot.available_parking_lots, count)

        elif action_key=="Vehicle_registration_number_for_driver_of_age":
            driver_age = action_command.split(' ')[-1]
            registration_numbers = parking_lot.get_registration_nos_by_age(driver_age)
            slot_nos = parking_lot.get_slot_numbers_by_age(driver_age)
            if slot_nos:
                print("Car with vehicle registration number "+format(registration_numbers)+" has been parked at slot number "+format(slot_nos))
