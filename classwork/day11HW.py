
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