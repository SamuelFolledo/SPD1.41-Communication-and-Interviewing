'''1.	Given a list of n numbers, determine if it contains any duplicate numbers.'''
def has_duplicates(arr):
    arr_set = set(arr) #turn array into a set which does not contain duplicate elements
    return len(arr) ==  len(arr_set) #returns true if length are still the same

array_with_duplicates = [1,2,3,3,4,5]
array_without_duplicates = [1,2,3,4,5]
print(has_duplicates(array_with_duplicates))
print(has_duplicates(array_without_duplicates))


'''2.	Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.'''




'''3.	Find the longest substring of unique letters in a given string of n letters.'''