#!/usr/bin/env python
# Calculate factorial of given number using an array of previously calculated values
from timer import Timer

_prev_values = [1]

#My Factorial function
def my_factorial(n):
    global _prev_values
    if len(_prev_values) > n:
        return _prev_values[n]
    f = 1
    if n > 1:
        f = n * my_factorial(n - 1)
    _prev_values.append(f)
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
