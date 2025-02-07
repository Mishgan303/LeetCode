class Solution(object):
    def climbStairs(self, n):
        k = 0
        l = []
        for i in range(1, n + 1):
            if i == 1:
                l.append(i)
                if n == 1:
                    return 1
            elif i == 2:
                l.append(i)
                if n == 2:
                    return 2
                l.append(i)
            else:
                k = l[i - 3] + l[i - 2]
                l.append(k)
        return l[-1]