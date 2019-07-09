class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k=math.sqrt(c)
        for i in range(0,int(k)+1):
            re=math.sqrt(c-i**2)
            if(re.is_integer()):
                return True
        return False