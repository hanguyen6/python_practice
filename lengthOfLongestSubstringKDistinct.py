# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
# Brute-force solution:
# Get all substrings from the string
# Calculate number of distinct characters 
# Filter substrings having k distinct characters 
# Get length of the substrings and return the longest length 
# O(N^2) for time complexity to get all substrings 

# Use two pointers and siding window:
# Try to contract or expand window of substring as traversing through the string 
# As substring contain less than k distinct character then we expand substring to the right 
# As expanding substring contains more than k distinc character, we contract the substring from the left 
# Keep track of longest substring while sliding the window 
# O(N*K) for time complexity
### worst case O(N*K) happens for string like "aaaaaabbbbbbbaaaaa" , k = 1 
# O(K) for space needed for hashtable 
class Solution(object):
    
    
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        m = {}
        longest_len = 0 
        
        while l <= r and r < len(s) :
            
            # Update character occurence 
            c = s[r]
            if (c in m.keys()):
                m[c] +=1 
            else:
                m[c] = 1 
            
            sub = s[l:r+1]
            #print("Checking substring " + sub)
            
            # Get distinct character from substring when distinct chars of substring reach to k 
            if (len(m) <= k):
                # print("matched with len ",  str(len(sub)))
                longest_len = max(longest_len, len(sub))
            elif (len(m) > k):
                # print("larger than k: " + sub)
                # Contract window until number of distinct character at most k 
                while (len(m) > k):
                    # print("Checking m: " + str(m))
                    c = s[l]
                    # print("remove left most char: " + c )
                    if (m[c] > 0):
                        # print("reduce occurence from m")
                        m[c] -=1
                    if (m[c] == 0):
                        # print("delete " + c)
                        del(m[c])
                    l+=1
        
            r+=1
    
        return longest_len
