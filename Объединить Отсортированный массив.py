class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ind = m 
        for i in nums2:
            nums1[ind] = i
            ind += 1
        nums1 = nums1.sort()
        return nums1

