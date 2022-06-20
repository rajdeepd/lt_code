from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        _len =len(nums)
        if k < _len:
            temp = nums[_len-k:]
            temp2 = nums[:_len-k]
            print('nums:', nums)

            for i in range(0,k):
                nums[i] = temp[i]

            for j in range(k,_len):
                index= j-(k)
                nums[j] = temp2[index]
        if k > _len:
            _k = k - _len
            self.rotate(nums,_k)

        print('nums rotated', nums)
        print('-----')

sol =  Solution()
nums = [-1,-100,3,99]

k = 2
#sol.rotate(nums,k)

#nums = [1,2,3,4,5,6,7]
#k = 2
#nums = [-1]
#k = 2
nums = [1,2]
k = 3
# k = k - _len

sol.rotate(nums,k)