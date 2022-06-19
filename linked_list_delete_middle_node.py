# Definition for singly-linked list.
from typing import Optional
import math
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        print(head.next)
        n = head
        count = 0
        while True:
            #print(n.next)
            n = n.next
            count += 1
            if n is None:
                break
        print(count)
        _middle = count/2
        even = False
        print(_middle)
        if _middle % 2 == 0:
          even = True# Even 
        else:
          even = False # Odd
        #middle = 0
        if even:
            middle = _middle
        else:
            middle = math.floor(_middle)
        print(middle)
            