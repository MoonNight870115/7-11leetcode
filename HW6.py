class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        a=[]
        for i in range (len(s)-1,-1,-1):
            a.append(s[i])
        while a:
            k = a.pop()
            if k=='M':
                res+=1000
            if k=='D':
                res+=500
            if k=='C':
                if a:
                    if a[-1]=='M':
                        a.pop()
                        res+=900
                    elif a[-1]=='D':
                        a.pop()
                        res+=400
                    elif a[-1]!='M' and a[-1]!='D':
                        res+=100
                else:
                    res+=100
            if k=='L':
                res+=50
            if k=='X':
                if a:
                    if a[-1]=='C':
                        a.pop()
                        res+=90
                    elif a[-1]=='L':
                        a.pop()
                        res+=40
                    elif a[-1]!='C' and a[-1]!='L':
                        res+=10
                else:
                    res+=10
            if k=='V':
                res+=5
            if k=='I':
                if a:
                    if a[-1]=='X':
                        a.pop()
                        res+=9
                    elif a[-1]=='V':
                        a.pop()
                        res+=4
                    elif a[-1]!='X' and a[-1]!='V':
                        res+=1
                else:
                    res+=1
        return res