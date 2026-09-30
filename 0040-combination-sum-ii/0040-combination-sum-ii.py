class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        l = []
        candidates.sort()

        def solve(start, current):

            if sum(current) == target:
                l.append(current[:])
                return

            if sum(current) > target:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                solve(i + 1, current)

                current.pop()

        solve(0, [])
        return l