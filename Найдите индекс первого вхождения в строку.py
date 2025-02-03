class Solution(object):
    def strStr(self, haystack, needle):
        dlina_1 = len(haystack)
        dlina_2 = len(needle)

        for i in range(dlina_1):
            if haystack[i] == needle[0]:
                if haystack[i:i + dlina_2] == needle:
                    return i
        return -1