class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # how do i decide which letters in s to replace
        # hwo do i decide what the letters is replaced to
        
#         if k == 0:
#             count = 1
#             max = 0
#             dict = {}
            
#             for i in range(len(s)):
#                 if s[i] not in dict and len(dict) == 0:
#                     dict[s[i]] = count
#                 elif s[i] not in dict and len(dict) > 0:
#                     count = 1
#                     max = len(dict)
#                     dict = {}
#                     dict[s[i]] = count
                    
#                 count += 1
#                 dict[s[i]] = count
                
#             return max
        
#         if k == len(s):
#             return k            
            
#         # find substring with most # of duplicates AND at most k number of non-duplicates
#         # output =  # of duplicates + k
        
#         dict = {}
#         count = 0
#         result = 0
        
#         for i in range(len(s)):
#             if s[i] not in dict: #and len(dict) < k:
#                 dict[s[i]] = 1
#             if s[i] in dict:
#                 dict[s[i]] += 1
#                 if dict[s[i]] == k and  i < len(s) and s[i+1] in dict:
#                     for j in range(len(dict)):
#                         result += dict[s[j]]
#                         result += 1
        
#         return result
        
        count = {}
        result = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            result = max(result, r - l + 1)
        
        return result
        
        
        
        
        
        