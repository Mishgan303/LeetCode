class Solution(object):
    def romanToInt(self, s):
        slovar_rim = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        k = []
        x = 0
        r = 0
        for i in s:
            if r == 1:
                r = 0
                continue
            if x <= len(s):
                x += 1
            if x == len(s):
                k.append(slovar_rim[i])
            for b in s[x:]:
                if slovar_rim[i] < slovar_rim[b]:
                    x += 1
                    r = 1
                    if i == 'I':
                        if b == 'V':
                            k.append(4)
                            break
                        elif b == 'X':
                            k.append(9) 
                            break
                    if i == 'X':
                        if b == 'L':
                            k.append(40)
                            break
                        elif b == 'C':
                            k.append(90) 
                            break
                    if i == 'C':
                        if b == 'D':
                            k.append(400)
                            break
                        elif b == 'M':
                            k.append(900) 
                            break
                    
                k.append(slovar_rim[i])
                break
        otvet = 0
        for p in k:
            p = int(p)
            otvet += p
        return otvet