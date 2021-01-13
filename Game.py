#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

number = random.randint(0, 10)
inputNumber = int(input("How many chances you want enter from 1 to 9? "))

if inputNumber in range(1,10):
    print("You {} chances left".format(inputNumber))
else:
    inputNumber = random.randint(1,10)
    print("You have {} chances left".format(inputNumber))


trys = int(input("Enter a number from 0 to 10: "))
trials = 1
while trys != number and trials < inputNumber:

    if trys < number:
        print("Too Low")
    else:
        print("Too High")

    trys = int(input("Try again, Enter a number from 0 to 10: "))
    trials = trials + 1
    print("Your remaining chances: ", inputNumber - trials)
if trys == number:
    print("Nice, you got the correct number")
else:
    print("Unfortunatly, the correct number was: " , number)

