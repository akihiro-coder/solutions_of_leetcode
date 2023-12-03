class Solution:
    def removeElement(self, nums: [int], val :int) -> int:
        not_equal_to_val = []
        for num in nums:
            if num != val:
                not_equal_to_val.append(num)
        return len(not_equal_to_val)
