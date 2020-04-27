# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
# Example 1:
#  message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
# reverse_words(message)
# # Prints: 'steal pound cake'
# print(''.join(message))

# Example 2:
  # the eagle has landed
sample2 = [ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
  'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ]

def reverse_words(message):
    # 1) reverse all the characters in the entire message to give us the right word order but with each word backward
    reverse_characters(message, 0, len(message)-1) #making message ['d', 'e', 'd', 'n', 'a', 'l', ' ', 's', 'a', 'h', ' ', 'e', 'l', 'g', 'a', 'e', ' ', 'e', 'h', 't']
    print("REV =",message)
    # Now reverse each word's characters
    current_word_start_index = 0

    # 2) Reverse the characters in each individual word.
    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '): #if i is not the end or message[i] is not a space
            reverse_characters(message, current_word_start_index, i - 1) 
            # If we haven't reached the end of the message our next word's start is one character ahead
            current_word_start_index = i + 1
    return message


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1

print(reverse_words(sample2)) #O(n) time and O(1) space!


# MERGE SORTED ARRAY

# Worst naive solution
def merge_sorted_lists(arr1, arr2): #O(nlogn) time complexity
    return sorted(arr1 + arr2)

# Second worst naive solution
#   - it doesnt cover some edge cases like if one list is longer than the other list
def naive_merge_lists(arr1, arr2):
    merged_list_size = len(arr1) + len(arr2)
    merged_list = [None] * merged_list_size #create an empty list

    arr2_index = 0
    arr1_index = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        first_unmerged_arr2 = arr2[arr2_index]
        first_unmerged_arr1 = arr1[arr1_index]

        if first_unmerged_arr1 < first_unmerged_arr2:
            # Case: next comes from arr1
            merged_list[current_index_merged] = first_unmerged_arr1
            arr1_index += 1
        else:
            # Case: next comes from arr2
            merged_list[current_index_merged] = first_unmerged_arr2
            arr2_index += 1

        current_index_merged += 1

    return merged_list

# BEST Solution: O(n) time and O(n) space
def merge_lists(arr1, arr2): 
    # Set up our merged_list
    merged_list_size = len(arr1) + len(arr2)
    merged_list = [None] * merged_list_size

    arr2_index = 0
    arr1_index = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_arr1_exhausted = arr1_index >= len(arr1)
        is_arr2_exhausted = arr2_index >= len(arr2)
        if (not is_arr1_exhausted and
                (is_arr2_exhausted or arr1[arr1_index] < arr2[arr2_index])):
            # Case: next comes from arr1, and checked if arr1 is not exhausted
            # arr1 must not be exhausted, and EITHER:
            merged_list[current_index_merged] = arr1[arr1_index]
            arr1_index += 1
        else:
            # Case: next comes from arr2 list
            merged_list[current_index_merged] = arr2[arr2_index]
            arr2_index += 1
        current_index_merged += 1

    return merged_list

print("Merged list =", merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])) #Should print [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]