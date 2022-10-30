class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in d:
                return [dic[t], i]
            dic[num] = i
        return []