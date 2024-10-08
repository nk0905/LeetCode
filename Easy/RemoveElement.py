# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                nums[i] = nums[k-1]
                nums[k-1] = '_'
                k -= 1
                i -= 1
            i += 1
        return k
        