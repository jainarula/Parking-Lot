# Parking-Lot Design

The important constraints that needs to be taken care of.
We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in     the slots allocated to them).


The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

The following files have problem solved using heap function.

The parking-system.design has the pseudo code for hashmap
while The parking_lot.py has solution of the problem using Heap Function.

The parking lot script contains a class for the car and parking lot. 
Car : registration Number and driver
Parking Lot : registration slot mapping, age registration mapping, slot car mapping, car number registration mapping, available parking lots

I am checking the status of the parking slot, assigning the closest slot, parking car and executing remove of a occupied slot if required.
The script also includes various other functionalities like getting registration number by age, slot number by age, slot number by registration number.
