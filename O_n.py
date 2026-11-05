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

def linearSearch(lst: list[int], target: int) -> int:
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None

print(calculateTime(linearSearch, list_5, 3))
print(calculateTime(linearSearch, list_10, 7))
print(calculateTime(linearSearch, list_100, 30))
print(calculateTime(linearSearch, list_1000, 500))
