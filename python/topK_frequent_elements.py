from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums) + 1
        arr = []
        for num, count in count.items():
            arr.append([count, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res