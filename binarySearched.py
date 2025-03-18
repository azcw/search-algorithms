import random

data = random.sample(range(100), 20)
data.sort()
print(data)

key = int(input("Enter key to search: "))

lo = 0
hi = len(data) - 1

def binarySearch(data, key, lo, hi):
    f = False
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == key:
            return "found at", mid
            f = True
        elif data[mid] < key:
            lo = mid + 1
        elif data[mid] > key:
            hi = mid - 1
    if f == False:
        return "Not Found"
    
print(binarySearch(data, key, lo, hi))