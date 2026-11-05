import random
import time

list_5 = [random.randint(1, 100) for _ in range(5)]
list_10 = [random.randint(1, 100) for _ in range(10)]
list_100 = [random.randint(1, 1000) for _ in range(100)]
list_1000 = [random.randint(1, 1000**10) for _ in range(1000)]

def calculateTime(func, lst: list, *args) -> float:
    start = time.perf_counter()
    func(lst, *args)
    end = time.perf_counter()
    return end - start

def accessFirstElement(lst: list[int]) -> int:
    return lst[0]

print(calculateTime(accessFirstElement, list_5))
print(calculateTime(accessFirstElement, list_10))
print(calculateTime(accessFirstElement, list_100))
print(calculateTime(accessFirstElement, list_1000))