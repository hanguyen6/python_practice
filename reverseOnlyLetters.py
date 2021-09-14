"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""
# Stack solution 
# O(N) for time and space complexity 
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Keep a stack for alpha character 
        stack = [c for c in s if c.isalpha()]
    
        # While traversing through string, 
        # update returning char array either element from stack 
        # or the non-alpha character from string
        ans = [stack.pop() if c.isalpha() else c for c in s]
    
        return "".join(ans)
    
# Two pointers solution 
# O(N) time and space complexity 
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Use two pointers, starting from both end of the string 
        l = 0
        r = len(s) - 1 
        str_array = [c for c in s]
        
        while (l <= r):
            # Move pointers to the postion of an English letter   
            while (l < len(s) and (s[l].lower() > 'z' or s[l].lower() < 'a')):
                l+=1
            while (r > 0 and (s[r].lower() > 'z' or s[r].lower() < 'a')):
                r-=1
            # Swap characters 
            if (l < r):
                tmp = str_array[l]
                str_array[l] = str_array[r]
                str_array[r] = tmp
            # Advance both pointers to new positions for next iteration 
            l+=1
            r-=1
        
        return "".join(str_array)
            
            
                
        
