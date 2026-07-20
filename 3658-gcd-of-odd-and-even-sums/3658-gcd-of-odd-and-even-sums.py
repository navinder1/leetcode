class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = n * (n + 1)
        odd = n * n

        while odd != 0:
            even, odd = odd, even % odd

        return even