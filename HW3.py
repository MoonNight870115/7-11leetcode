class Solution:
    def rotatedDigits(self, N: int) -> int:
        cou = 0
        ro = ['2','5','6','9']
        dro = ['3','4','7']
        for i in range(1,N+1):
            s = str(i)
            if len(set(s).intersection(set(ro))) != 0:
                if len(set(s).intersection(set(dro))) == 0:
                    cou +=1
        return cou