import random
import time


def calculateTime(func, n: int) -> float:
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(calculateTime(fibonacci, 5))
print(calculateTime(fibonacci, 10))
print(calculateTime(fibonacci, 100))
print(calculateTime(fibonacci, 1000))