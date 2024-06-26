#Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Using Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
                print(map)
            map[n]= i


# Using list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_arr = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_arr:
                return [diff_arr.index(diff), i]
            diff_arr.append(n)
