#MoveZeroes
class Solution():
    def moveZeroes(self,nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[pos],nums[i] = nums[i],nums[pos]
                pos += 1                
        return nums