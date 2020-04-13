'''1.	Given a list of n numbers, determine if it contains any duplicate numbers.'''
def has_duplicates(arr):
    arr_set = set(arr) #turn array into a set which does not contain duplicate elements
    return len(arr) ==  len(arr_set) #returns true if length are still the same

array_with_duplicates = [1,2,3,3,4,5]
array_without_duplicates = [1,2,3,4,5]
print("List: ",array_with_duplicates, " has duplicates=", has_duplicates(array_with_duplicates))
print("List: ",array_without_duplicates, " has duplicates=", has_duplicates(array_without_duplicates))


'''2.	Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)
    
    def print_list(self): 
        temp = self.head 
        while (temp): 
            print(temp.data, "->")
            temp = temp.next

    def append(self, item): #insert Node at the end
        newNode = Node(item)
        if self.head == None: #if head is empty, then append to head
            self.head = newNode
            self.tail = newNode
            return
        else: #point tail's next to newNode and assign newNode as the new tail
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, item): #insert Node at the beginning
        newNode = Node(item) #create a node with that item
        if self.head == None: #if list is empty...
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head #point newNode's next to current head
        self.head = newNode #assign newNode as the head

#ANSWER
    def get_middle(self): #return an array of Node; if length of LL is odd, return 1 Node, 2 Nodes if even
        if self.head == None: #if head is empty, then append to head
            return None
        #1) get the length of the list
        length = 0 
        temp = self.head
        while temp: #while temp is not nil
            length += 1 #increment counter
            temp = temp.next
        #2) create properties
        temp = self.head #reset head
        half = length // 2 + (length % 2 > 0) #gets half and round up if array length is odd
        #3) look for middle
        while half > 1: #to stop and get the middle, loop until half is 1
            temp = temp.next
            half -= 1
        if length % 2 == 0: #if length is even (remainder is 0), return 2 data
            return [temp.data, temp.next.data]
        return [temp.data]

odd_ll = LinkedList([1,2,3,4,5]) #create ll from list of numbers
print("Odd LL's middle=",odd_ll.get_middle())
even_ll = LinkedList([1,2,3,4,5,6])
print("Even LL's middle=",even_ll.get_middle())


#These HW problems makes no sense so I did 1 and 2
'''3.	Find the longest substring of unique letters in a given string of n letters.'''

'''4.   Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.'''