class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _dict = []

        for n in nums:
            if n in _dict.keys():
                _dict[n] = _dict[n] + 1
            else:
                _dict[n] = 1


        for key, value in _dict.items():
            if 1 == value:
                return key

