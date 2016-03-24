#!/usr/bin/env python
# Calculate factorial of given number using python factorial function
from math import *
from timer import Timer

# Main program
while True:
    try:
        number = input("Enter a non-negative integer (ctrl-c to quit): ")
    except:
        break
    try:
        n = int(number)
        if number == n and n >= 0:
            with Timer() as t:
                print str(n) + "! = " + str(factorial(n))
            print "=> elapsed time: %f ms" % t.msecs
    except:
        continue
