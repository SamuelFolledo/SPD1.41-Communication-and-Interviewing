# given 2 strings, if t is anagram of s
# hello llohe -> true

str1 = "anagram"
anagram = "nagaram"

def is_anagram(str1, anagram):
    #loop through each char in str
    for char in str1:
        # check if char is in anagram
        # get index of char

        # if index == -1, 
        # if char in anagram:
            #then remove that anagram
            # anagram.replace(char, "")
        else:
            return False
    # if anagram is empty then return true
    print(anagram)
    return len(anagram) == 0

print(is_anagram(str1, anagram))

print(anagram)
# inputs str=anagram, anagram=nagaram
# char=a, anagram = nagram
# char=n, anagram = agram
# char=a, anagram = gram
# char=g, anagram = ram
# char=r, anagram = am
# char=a, anagram= m
# char=m, anagram=""
# len(anagram) ==0, this will return True

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(6)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
node.next.next.next.next.next = ListNode(5)
node.next.next.next.next.next.next = ListNode(6)