# class Solution:
#     def gcdSum(self, nums: list[int]) -> int:
#         max1 = 0
#         l=[]
#         for i in range(1, len(nums) + 1):
#             m = max(nums[:i])
#             n = nums[i - 1]
#             while n != 0:
#                 m, n = n, m % n
#             l.append(m)
#         l.sort()
#         print(l)
#         left=0
#         right=len(l)-1
#         res=[]
#         while(left<right):
#             a=l[left]
#             b=l[right]
#             while b!=0:
#                 a,b=b,a%b
#             res.append(a)
#             left+=1
#             right-=1
#         return sum(res)
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        
        n_len = len(nums)
        l = [0] * n_len
        curr_max = nums[0]
        
        for i in range(n_len):
            val = nums[i]
            if val > curr_max:
                curr_max = val
            l[i] = math.gcd(curr_max, val)
            
        l.sort()
        
        res_sum = 0
        left = 0
        right = n_len - 1
        
        while left < right:
            res_sum += math.gcd(l[left], l[right])
            left += 1
            right -= 1
            
        return res_sum
