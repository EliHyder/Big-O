
import time

list_5 = [i for i in range(5)]
list_10 = [i for i in range(10)]
list_100 = [i for i in range(100)]
list_1000 = [i for i in range(1000)]

def calculateTime(func, lst: list, *args) -> float:
    start = time.perf_counter()
    func(lst, *args)
    end = time.perf_counter()
    return end - start

def binarySearch(lst: list[int], target: int) -> int:
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

print(calculateTime(binarySearch, list_5, 3))
print(calculateTime(binarySearch, list_10, 7)) 
print(calculateTime(binarySearch, list_100, 30))
print(calculateTime(binarySearch, list_1000, 700))