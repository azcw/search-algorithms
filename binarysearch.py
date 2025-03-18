import random
data = []
data = random.sample(range(100),20)
data.sort()
print(data)

k = int(input("Enter The Number To Be Found: "))

def binary(array, low, high, target):
    while low <= high:
        mid = (high + low) // 2 
        if target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
        else:
            return "Found At Index:", mid
    return "Not Found"
text = binary(data, 0, len(data)-1, k)
print(text)