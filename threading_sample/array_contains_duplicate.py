class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _set = set()
        for n in nums:
            if n in _set:
                return True
            else:
                _set.add(n)

