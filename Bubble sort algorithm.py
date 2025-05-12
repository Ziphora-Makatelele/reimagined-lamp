my_array = [17, 23, 96, 68, 2, 75, 12, 20]

n = len((my_array))
    for i in range (n-1)
        if my_array[j]>my_array[j+1]:
        my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
        
print("Sorted array: ", my_array)