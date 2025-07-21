from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            a[s].append(word)
        return list(a.values())