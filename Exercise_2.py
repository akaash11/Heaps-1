# S30 Problem #84 Merge k Sorted Lists
#LeetCode #23 https://leetcode.com/problems/merge-k-sorted-lists/description/

# Author : Akaash Trivedi
# Time Complexity : O(N log k)
# Space Complexity : O(k)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# merge 2 list then add third and so on
# Time complexity: O(nk^2)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        merged = ListNode(float('-inf'))
        for l in lists:
            merged = self.mergeLinkedList(merged,l)
        return merged.next
    
    def mergeLinkedList(self, l1, l2)->Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next 
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next


# priority queue solution    
# Time Complexity: O(nk log k)
# O(log k) to push/pop. k is number of lists
# n - number of node in each list
# Space compleaxity O(k)
# wappper class to override ListNode __lt__ ("less than" function)
class Wrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        res = ListNode(0) # dummy node to return
        # work on curr node as we have to return the head
        curr = res

        # add all the head node to minHeap
        for head in lists:
            if head:
                heapq.heappush(minHeap, Wrapper(head))
        
        while minHeap:
            # pop the min from heap
            tempMin = heapq.heappop(minHeap)
            curr.next = tempMin.node # add min to currs next
            curr = curr.next
            # if the list that popped has next element, then add to heap
            if tempMin.node.next:
                heapq.heappush(minHeap, Wrapper(tempMin.node.next))
            
        return res.next
