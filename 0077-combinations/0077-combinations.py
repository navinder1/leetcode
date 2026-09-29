class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[]
        def solve(start,current):
            if(len(current)==k):
                l.append(current[:])
                return
            for i in range(start,n+1):
                current.append(i)
                solve(i+1,current)
                current.pop()
        solve(1,[])
        return l