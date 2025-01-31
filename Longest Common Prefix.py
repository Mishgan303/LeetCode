class Solution(object):
    def longestCommonPrefix(self, strs):
        k = 0
        otvet = ''
        while True: 
            i = strs[0][0:k + 1]
            k += 1
            kolichestvo = 0
            for slova in strs:
                if slova.startswith(i):
                    kolichestvo +=1
                    continue

            if kolichestvo == len(strs):
                otvet = i
            else:
                return otvet
        return otvet