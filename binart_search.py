class Solution:
    def search(self, nums, target: int) -> int:
        alist = nums

        first = 0
        last = len(alist) - 1
        found = False

        while first <= last and not found:
            pos = 0
            midpoint = (first + last) // 2
            if alist[midpoint] == target:
                pos = midpoint
                found = True
            else:
                if target <= alist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if found == False:
            return -1
        else:
            return pos

