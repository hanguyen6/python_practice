# https://leetcode.com/problems/subdomain-visit-count/submissions/
# O (N) for time and space complexity 
from collections import Counter 

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domainVisits = Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                    domainVisits[".".join(frags[i:])] += count
        return [ "{} {}".format(ct, dom) for dom, ct in domainVisits.items()]
                
                
        
