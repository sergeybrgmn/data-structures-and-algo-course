"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

#The target solution using recursion
def get_fib(position):
    if position <=1:
        return position
    else: 
        return (get_fib(position-2) + get_fib(position-1))

#That was my first fib code, because was hard to solve in recursion
def get_fib_rigid(position):
    prev = 0
    curr = 1
    pos = 2
    if position <= 1:
        return position
    else:
        while pos <= position:
            fib = prev + curr
            prev = curr
            curr = fib
            pos += 1
        return fib



# Test cases
print(get_fib(9))
print(get_fib(7))
print(get_fib(3))