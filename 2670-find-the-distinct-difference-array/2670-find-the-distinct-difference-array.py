class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return res
        