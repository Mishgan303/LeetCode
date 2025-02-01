class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        flag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1

        return flag