class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if list1 == [] and list2 == []:
            return []

        for num in list2:
            list1.append(num)
        sorted_list = sorted(list1)

        return sorted_list
