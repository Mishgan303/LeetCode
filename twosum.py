class Solution(object):
    def twoSum(self, nums, target):
        nums = list(nums)
        target = int(target)
        for i in nums:
            for b in nums[nums.index(i) + 1:]:
                summ = i + b
                if summ == target:
                    if i == b:
                        return [index for index, value in enumerate(nums) if value == i]
                    return [nums.index(i), nums.index(b)]
