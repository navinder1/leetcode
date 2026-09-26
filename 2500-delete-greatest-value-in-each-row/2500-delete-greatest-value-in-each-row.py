class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:

        res = []

        while len(grid[0]) > 0:
            s = []

            for i in range(len(grid)):
                max1 = max(grid[i])
                s.append(max1)
                grid[i].remove(max1)

            res.append(s)

        sum1 = 0

        for row in res:
            sum1 += max(row)

        return sum1