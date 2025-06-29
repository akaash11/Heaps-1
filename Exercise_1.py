# S30 Problem #83 Kth Largest Element in an Array
#LeetCode #215 https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Author : Akaash Trivedi
# Time Complexity : O(n log k)
# Space Complexity : O(k) k is heap space
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using min heap to clone
        minheap = []
        for n in nums:
            heapq.heappush(minheap, n)
            # only store k elements in stack, 
            # as everything else would be surely smaller
            if len(minheap) > k:
                heapq.heappop(minheap)  
        #print(minheap)
        return heapq.heappop(minheap)
