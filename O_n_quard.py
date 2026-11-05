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


def bubbleSort(lst: list[int]) -> list[int]:
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(calculateTime(bubbleSort, list_5))
print(calculateTime(bubbleSort, list_10))
print(calculateTime(bubbleSort, list_100))
print(calculateTime(bubbleSort, list_1000))