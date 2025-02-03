class Solution(object):
    def lengthOfLastWord(self, s):
        k = 0
        probel = 0
        for i in s[-1::-1]:
            if k != 0 and i == ' ':
                return k
            elif i.isalpha():
                k += 1
        return k    
        