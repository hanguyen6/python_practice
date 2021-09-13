## Use a dictionary to keep track of non-zeros element with its index 
## While taking dot product, use elements in the dictionary 
# O(N) for time complexity 
# O(M) for space needed of hash map 
class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        ## Define local variable 
        self.nonZeros = {}
        for i, n in enumerate(nums):
            if (n != 0):
                self.nonZeros[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for i, n in self.nonZeros.items():
            if i in vec.nonZeros.keys():
                res += vec.nonZeros[i] * n
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
