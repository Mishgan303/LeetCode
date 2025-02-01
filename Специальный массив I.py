class Solution(object):
    def isArraySpecial(self, nums):
        dlina = len(nums)
        flag = 0
        for i in nums:
            prov = i % 2
            if prov == 0:
                if flag != 1:
                    flag = 1
                else:
                    return False
            else:
                if flag != 2:
                    flag = 2
                else:
                    return False
        return True