from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        for num in nums:
            if num in sets:
                return True
            sets.add(num)
        return False
    


if __name__ == "__main__":
    sol = Solution()
    # Example test cases
    print(sol.containsDuplicate([1, 2, 3, 4])) # False
    print(sol.containsDuplicate([1, 2, 3, 1])) # True