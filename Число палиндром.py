class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if len(x) >= 1:
            x_palindrom = x[-1::-1]
            for i in range(len(x)):
                if x_palindrom == x:
                    return True
                else:
                    return False
            return False