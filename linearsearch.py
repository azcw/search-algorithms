import random
array = []
for x in range(30):
    num = random.randint(1, 100)
    array.append(num)
print(array)

def linearSearch(lookingFor):
    f = False
    for count in range(len(array)):
        num = array[count]
        if num == lookingFor:
            print("Found at index: ", count)
            f = True
    if f == False:
        print("Not found")
        
            
lookingFor = int(input("What number are you looking for? "))
linearSearch(lookingFor)