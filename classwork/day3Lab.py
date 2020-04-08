
# find k largest number in array, return in decreasing
# [3,4,5,8,6,9];
def sort_descending(arr):
    temp = 0 #store current num
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1): #-1 to never go out of range
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1] #moves right to left
                arr[i+1] = temp #moves left to right
                isSorted = False
    print(arr)

sort_descending([3,-2,-9,9,6])