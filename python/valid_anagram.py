class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for char in s:
            tracker[char] = tracker.get(char, 0) + 1
        for char in t:
            if char not in tracker:
                return False
            tracker[char] -= 1
        for c in tracker.values():
            if c != 0:
                return False
        return True
    

'''
I seen that I could populate a hashmap and just do the same removing the elements backwards.
I could've added a case guard clause as well
checking for the length as well.
'''