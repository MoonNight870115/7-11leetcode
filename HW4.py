#Find All Numbers Disappeared in an Array
class Solution():
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = set(sorted(nums))
        u = range(1,len(nums)+1)
        if len(l) > 0:
            return list(set(u) - l)
        else:
            return []