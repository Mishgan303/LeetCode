class Solution(object):
    def mySqrt(self, x):
        k = 0
        while True:
            k += 1
            koren_x = k * k
            if koren_x == x:
                return k
            elif koren_x < x:
                continue
            elif koren_x > x:
                return k - 1
            