class Solution(object):
    def searchInsert(self, nums, target):
        dlina = len(nums)

        for i in range(dlina - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target < nums[i + 1]:
                return i + 1

        return dlina