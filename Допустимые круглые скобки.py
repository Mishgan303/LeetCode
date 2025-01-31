class Solution(object):
    def isValid(self, s):
        slovar = {'(': ')', '{': '}', '[': ']'}
        flag = 0
        for i in s:
            for b in list(slovar):
                if i == b:   
                    if slovar.get(b) in s:
                        flag += 1
                        continue
                    else:
                        return False

        if flag == (len(s) // 2):
            return True 
        else:
            return False        