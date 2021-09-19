# https://leetcode.com/problems/majority-element/solution/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Get a random number 
# Count the random number in the list 
# If count is majority count then return the random number 
# else Retake another random number
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums) / 2
        while True:
            rd = random.choice(nums)
            elem_count = sum(1 for elem in nums if elem == rd)
            if (elem_count) > majority_count:
                return rd 

# O(1) space and O(n) time complexity 
# Use a variable to keep track of the majority candidate  
# As traversing through the list
    # As count = 0, choose majority candidate as the number at current traversing position  
    # If current number equals the candidate, add 1 to count  
    # If not, reduce 1 to count 
# Since there is a majority number in the list, it will be the latest one in the variable 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None 
        for num in nums:
            if (count == 0):
                candidate = num
            if (candidate == num):
                count +=1 
            else:
                count -=1
        
        return candidate
        
            
        
