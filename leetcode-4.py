# leetcode 4

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        m, n = 0, 0
        while m < len(nums1) and n < len(nums2):
            if nums1[m]<nums2[n]:
                arr.append(nums1[m])
                m+=1
            elif nums1[m]>nums2[n]:
                arr.append(nums2[n])
                n+=1
            elif nums1[m]==nums2[n]:
                arr.append(nums1[m])
                m+=1
                n+=1
        arr.extend(nums1[m:])
        arr.extend(nums2[n:])
        res = []
        for num in arr:
            if num not in res:
                res.append(num)
        print(res)
        if len(res) % 2 == 0:
            return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2
        else:
            return res[len(res) // 2]
