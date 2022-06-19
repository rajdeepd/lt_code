class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        answer = None
        for n in nums:
            #print(len(nums))
            #print(count)
            #print("--")
            #print(len(nums) - count > 1)
            if (len(nums) - count > 1):
                print(n == nums[count + 1])
            print("n:" + str(n))
            if  (len(nums) - count > 1) and not (n == nums[count + 1]):
                #print('inside')

                print(nums[count - 1])
                #print("***")
                if n != nums[count -1]:
                    answer = n
                    print(answer)
                    break
            elif len(nums) - count == 1:
                #print("here")
                if len(nums) == 1:
                    answer = n
                    break
                if n != nums[count - 1]:
                    answer = n
                    #print(answer)
                    break
            count = count + 1

        return answer


if __name__ == "__main__":
    s = Solution()
    #nums = [1, 1, 2,2, 3, 3, 4, 4, 8]
    nums = [1]
    response = s.singleNonDuplicate(nums)
    print(response)