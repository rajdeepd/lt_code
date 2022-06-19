import math

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = left + math.floor((right - left) / 2)
        print('mid:',mid)
        print('nums[left] > target',nums[left] > target)
        while nums[left] < target:
            print(nums[left], nums[right], nums[mid])
            print('target:', target)
            if target > nums[mid]:
                if target < nums[mid+1]:
                    return mid+1
                print('nums[mid]',nums[mid])
                print('target', target)
                left = mid

            elif target == nums[mid]:
                return mid
            else:
                right = mid
            mid = left + math.floor((right - left) / 2)
            print('mid:', mid)
        return left

sol = Solution()
nums = [1,3,5,6]
target = 5
print(sol.searchInsert(nums, target))