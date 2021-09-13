 ## Dynamic Programming 
 ## O(N) time complexity and O(1) space 
 def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n < 3):
            return 1 if n else 0
        x, y, z = 0, 1, 1 
        for _ in range(n -2):
            x, y, z = y, z, x + y + z 
        return z
 
 # Caching with hash table
class Solution(object):
        
    def __init__(self):
        self.m = {0:0, 1:1, 2:1} 
    
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n in self.m.keys()):
            return self.m[n]
        else:
            tmp = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            self.m[n] = tmp
            return tmp 
