#!/usr/bin/env python
# Calculate factorial of given number using a recursive method
from timer import Timer

#My Factorial function
def my_factorial(n):
    f = 1
    if n > 1:
        f = n * my_factorial(n - 1)
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
