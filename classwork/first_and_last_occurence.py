# 3) Given a sorted array, find the index of the first and last occurrence of a given element. If the given element is not found in the array, report that. 
num_list1 = [1,2,2,3] #n = 2 -> [1,2]
num_list2 = [1,2,3,3,4,5,5] #n = 3 -> [2,3] #n=4 -> [4] #n=5 -> [5,6]

#Solution 1
def find_first_last_occurence(list1, n):
    result = []
    for i in range(len(list1)):
        if list1[i] == n: #if we found our target
            if len(result) > 1: #if result's length > 1, then update index 1
                result[1] = i
            else: #append the first and second occurence
                result.append(i)
    return result
print("2.a) ",find_first_last_occurence(num_list2, 4),"\n")

#Solution 2
#with start and end going to middle
def find_first_last_occurence_b(list1, n):
    result = []
    start = 0
    end = len(list1) - 1
    # half = int(len(list1) // 2 + (len(list1) % 2 > 0)) #gets half and round up if array length is odd
    while start <= end:
        if list1[start] == n:
            result.append(start)
            break
        start+=1

    while end > start:
        if list1[end] == n:
            result.append(end)
            break
        end-=1
    return result

print("2.b)",find_first_last_occurence_b(num_list1, 1)) #num_list2, n = 3 -> [2,3] #n=4 -> [4] #n=5 -> [5,6]