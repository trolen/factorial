#!/usr/bin/env python
# Calculate factorial of given number using an iterative method
from timer import Timer

#My Factorial function
def my_factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

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
                print str(n) + "! = " + str(my_factorial(n))
            print "=> elapsed time: %f ms" % t.msecs
    except:
        continue
