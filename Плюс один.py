class Solution(object):
    def plusOne(self, digits):
        stroka = str()
        for i in digits:
            t= str(i)
            stroka += t
        stroka = int(stroka)
        stroka += 1
        stroka = str(stroka)
        spisok = []
        for k in stroka:
            k = int(k)
            spisok.append(k)
        return spisok