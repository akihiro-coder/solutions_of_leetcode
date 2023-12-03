import numpy as np

class Solution:
    def get_indicies(self, nums, target):
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return []

    def get_indicies2(self, nums, target):
        num_map = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            print(f'num_map : {num_map}')
            print(f'complement : {complement}')
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        return []


        

sol = Solution()
nums = [2,7,11,15]
target = 9
indicies_list = []
indicies_list.append(sol.get_indicies2(nums, target))
print(indicies_list)
