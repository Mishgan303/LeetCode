class Solution(object):
    def removeDuplicates(self, nums):
        dlin = len(nums)
        flag = 1
        for i in range(1, dlin):
            if nums[i] != nums[i-1]:
                nums[flag] = nums[i]
                flag += 1
             
        return flag 
