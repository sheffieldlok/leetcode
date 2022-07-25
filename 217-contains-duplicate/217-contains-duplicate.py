class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashset/hashmap
        # iterate through the array O(N)
        # check current iteration's element with hashset:
        # if does not exist --> add into hashset
        # else return false
        # return true
        
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] in dict: return True
            else: dict[nums[i]] = 1
                
        return False
            