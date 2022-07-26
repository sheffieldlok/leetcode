class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        
        # dict = {}
        # max_so_far = 0
        # max = 0
        
#         for i in range(len(s)):
#             if s[i] not in dict:
#                 dict[s[i]] = 1
#                 print("if dict: ", dict)
#             else:
#                 print("else dict: ", dict)
#                 max_so_far = len(dict)
#                 print("len_dict: ", len(dict))
#                 print("max_so_far: ", max_so_far)
#                 if max_so_far > max:
#                     max = max_so_far
#                 dict = {}
#                 dict[s[i]] = 1
            
#         if len(dict) > max: 
#             return len(dict)

#         for i in range(len(s)):
#             dict[s[i]] = 1
#             for j in range(i+1, len(s)):
#                 if s[j] not in dict:
#                     dict[s[j]] = 1
#                     print("if dict: ", dict)
#                 else:
#                     print("else dict: ", dict)
#                     max_so_far = len(dict)
#                     print("len_dict: ", len(dict))
#                     print("max_so_far: ", max_so_far)
#                     if max_so_far > max:
#                         max = max_so_far
#                     dict = {}
                    
#         if len(dict) > max:
#             return len(dict)
        
#         return max
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            # print("s[i]: ", s[i])
            # print("usedChar: ", usedChar)
            # print("start: ", start)
            # print("")
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
                # print("usedChar[s[i]]: ", usedChar[s[i]])
                # print("updated start: ", start)
                # print("")
            else:
                maxLength = max(maxLength, i - start + 1)
                # print("maxLength: ", maxLength)
                # print("")

            usedChar[s[i]] = i

        return maxLength
            
                                 
    
        
                                 