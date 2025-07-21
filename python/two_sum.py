from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in maps:
                return [maps[diff], index]
            maps[value] = index
        return []