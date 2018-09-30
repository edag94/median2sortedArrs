class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return self.findMedian( self.merge(nums1,nums2) )
    
    def findMedian(self, l):
        idxFront = 0
        idxBack = len(l)-1
        
        while not (idxFront == idxBack or idxBack - idxFront == 1):
            idxFront = idxFront + 1
            idxBack = idxBack - 1
            
        if idxFront == idxBack:
            return l[idxFront]
        else:
            return (l[idxFront] + l[idxBack])/2
            
        
    #merge both sorted arrays    
    def merge(self, l1, l2):
        idx1 = 0
        idx2 = 0
        len1 = len(l1)
        len2 = len(l2)
        outlist = []
        while(idx1 < len1 or idx2 < len2):
            #if at end of l1
            if not (idx1 < len1):
                outlist.append(l2[idx2])
                idx2 = idx2 + 1
            elif not (idx2 < len2):
                outlist.append(l1[idx1])
                idx1 = idx1 + 1
            else:
                if l1[idx1] > l2[idx2]:
                    outlist.append( l2[idx2] )
                    idx2 = idx2 + 1
                else:
                    outlist.append( l1[idx1] )
                    idx1 = idx1 + 1
        return outlist
        
                
            
if __name__ == '__main__':
    sol = Solution()
    sol.findMedianSortedArrays([1,3], [2])