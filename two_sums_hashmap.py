class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			difference = target - val
			if difference in mapping:
				return [mapping[difference], index]
			else:
				mapping[val] = index


	def twoSum2(self, nums, target: int):
		index = 0

		first = 0
		second = 0
		_len = len(nums)
		for i in range(0, _len - 1):
			print(i)
			for j in range(i + 1, _len):
				sum = nums[i] + nums[j]
				print(sum)
				print(sum == target)
				if sum == target:
					first = i
					second = j
					return [i, j]

		return [i, j]
s = Solution()
print(s.twoSum([2,7,11,15], 9))