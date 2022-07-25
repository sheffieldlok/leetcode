class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        
        # Find 3 numbers in array that add up to 0
        # 3 numbers have to be of different positions
        
#         result_local = [] # local result to be added into result_global
#         result_global = [] # final returned answer
#         dict = {}
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     p1 = nums[i]
#                     p2 = nums[j]
#                     p3 = nums[k]
                    
#                     if p1+p2+p3 == 0:
#                         result_local.append(p1)
#                         result_local.append(p2)
#                         result_local.append(p3)
#                         result_local.sort()
#                         if tuple(result_local) in dict:
#                             result_local = []
#                             break
#                         else:
#                             dict[tuple(result_local)] = 1
#                             result_global.append(result_local)
                        
#                     result_local = []
        
#         return result_global
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


                    
        
        
                