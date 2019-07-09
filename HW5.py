class Solution:
    def addDigits(self, num: int) -> int:
        k=num%9
        if num==0:
            ans=0
        if k==0 and num!=0:
            ans=9
        else:
            ans=k
        return ans