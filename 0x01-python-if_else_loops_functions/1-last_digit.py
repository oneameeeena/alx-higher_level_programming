#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if (number > 0):
    print("Last digit of {:d} is {:d}".format(number, last_digit))
elif (number < 0):
    print("Last digit of {:d} is {:d}".format(number, last_digit * -1))
else:
    print("Last digit of {:d} is {:d}".format(number, last_digit))

if (last_digit > 5):
    print("and is greater than 5")
elif (last_digit == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
