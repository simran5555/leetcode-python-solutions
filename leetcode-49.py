# leetcode 49
# group anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        result = []

        for s in strs:
            sorted_string = tuple(sorted(s))
            map[sorted_string].append(s)

        for val in map.values():
            result.append(val)

        return sorted(result)
