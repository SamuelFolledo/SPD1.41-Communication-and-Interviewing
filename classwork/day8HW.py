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

print(reverse_words(sample2))