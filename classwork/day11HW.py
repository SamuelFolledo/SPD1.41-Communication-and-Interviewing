
# merge sorted array
# https://leetcode.com/problems/merge-sorted-array/
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index1 = 0 #index for nums1
    index2 = 0 #index for nums2
    result = []
    while index1 < m and index2 < n: #loop until index1 and index2 is greater than m and n respectively
        if nums1[index1] <= nums2[index2]: #: #if num1 is less than num2, append num1 first
            result.append(nums1[index1])
            index1+=1
            if index1 == m: #check if we finished nums1, then append the rest of nums1
                result += nums2[index2:]
                break
        else:
            result.append(nums2[index2])
            index2+=1
            if index2 == n: #check if we finished nums1, then append the rest of nums2
                result += nums1[index1:]
                break
    return result

print(merge([1,2,4,4], 4, [-1,2,3,5], 3))






#HW2: https://leetcode.com/problems/remove-linked-list-elements/
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


def remove_elements(head, val):
    '''Remove all elements from a linked list of integers that have value val.
    Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
    '''
    while head: #handle head and next having the val
        if head.val == val:
            head = head.next
        else:
            break

    current = head
    prev = None

    while current: #loop til current is None
        if current.val == val: #if current has val, point prev's next to current.next
            prev.next = current.next
        prev = current
        current = current.next

    return head

# node = ListNode(6)
# node.next = ListNode(6)
# node.next.next = ListNode(2)
# node.next.next.next = ListNode(3)
# node.next.next.next.next = ListNode(4)
# node.next.next.next.next.next = ListNode(5)
# node.next.next.next.next.next.next = ListNode(6)

# node = remove_elements(node, 6)

node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)

node = remove_elements(node, 1)
while node:
    print(node.val)
    node = node.next