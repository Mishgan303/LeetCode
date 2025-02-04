class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        summ = a + b
        summ = bin(summ)
        summ = summ.lstrip("0b")
        return summ
        