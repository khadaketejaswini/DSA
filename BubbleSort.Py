#Go through the array one value at a time if you find the next value is smaller the swap and move the highest value to last
n = len(my_Array)
for i in range(n):
    for j in range(n-i-1):
        if my_Array[j] > my_Array [j+1] :
            my_Array[j], my_Array[j+1] = my_Array[j=1], my_Array[j]


print(my_Array)