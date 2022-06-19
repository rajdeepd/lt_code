class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        i = 0
        for n in nums:
            squares.append(n*n)
        return sorted(squares)