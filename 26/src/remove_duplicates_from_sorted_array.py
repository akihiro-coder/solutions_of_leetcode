class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        list_remove_duplicates = []
        for num in nums:
            if num not in list_remove_duplicates:
                list_remove_duplicates.append(num)
        num_remove_duplicates = len(list_remove_duplicates)
        return num_remove_duplicates
