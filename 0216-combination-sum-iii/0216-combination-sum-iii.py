class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        l = []

        def solve(start, current):
            if len(current) == k:
                if sum(current) == n:
                    l.append(current[:])
                return

            for i in range(start, 10):
                current.append(i)
                solve(i + 1, current)
                current.pop()

        solve(1, [])
        return l