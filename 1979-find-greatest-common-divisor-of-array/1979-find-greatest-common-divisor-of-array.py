class Solution:
    def findGCD(self, nums: List[int]) -> int:
        Min=min(nums)
        Max=max(nums)
        gcd=0
        for i in range(1,Max+1):
            if(Max%i==0 and Min%i==0):
                gcd=i
        return gcd


        