class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in dict:
                return [dict[m], i]
            else:
                dict[n] = i