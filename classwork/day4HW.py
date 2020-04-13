'''1.	Given a list of n numbers, determine if it contains any duplicate numbers.'''
def has_duplicates(arr):
    arr_set = set(arr) #turn array into a set which does not contain duplicate elements
    return len(arr) ==  len(arr_set) #returns true if length are still the same

array_with_duplicates = [1,2,3,3,4,5]
array_without_duplicates = [1,2,3,4,5]
print(has_duplicates(array_with_duplicates))
print(has_duplicates(array_without_duplicates))


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



'''3.	Find the longest substring of unique letters in a given string of n letters.'''