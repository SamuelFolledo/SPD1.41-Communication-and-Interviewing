
# array of number and a value, remove elements in O(1)
# arr= [3,2,2] val = 3 -> [2,2]
def remove_elements(arr, val, index = 0):
    if len(arr) - 1 <= index:
        return arr
    if val == arr[index]:
        arr.pop(index)
        return remove_elements(arr, val, index)
    else:
        return remove_elements(arr, val, index+1)
        
print(remove_elements([1, 1, 1, 1, 2, 1, 3, 1, 1, 4, 5, 1, 6], 1))