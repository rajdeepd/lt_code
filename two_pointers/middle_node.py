from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        count = 0
        # print(type(node))
        _list = []

        while node.next is not None:
            _list.append(node.val)
            node = node.next
            count += 1
        _list.append(node.val)

        _output = None
        len_list = len(_list)
        if len_list % 2 == 0:
            start = len_list / 2 + 1
        else:
            start = (len_list + 1) / 2

        for j in range(int(start), len_list + 1):

            if _output is None:
                _output = []
                _output.append(ListNode(val=_list[j - 1]))
            else:
                temp = ListNode(val=_list[j - 1])
                if _output[j - 1 - int(start)] is not None:
                    _output[j - 1 - int(start)].next = temp
                    _output.append(temp)
        return _output[0]
