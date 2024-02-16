#Fibonacci of 50
from functools import reduce

def fibonacci(count):
    sequence = (0, 1)

    for _ in range(2, count):#using lambda function
        sequence += (reduce(lambda a, b: a + b, sequence[-2:]), )

    return sequence[:count]
#printing output
print(fibonacci(50))
