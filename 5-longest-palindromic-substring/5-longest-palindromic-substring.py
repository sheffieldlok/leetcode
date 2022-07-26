class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]: return s # if the entire s is a palindrome itself
        
#         l = 0
#         result = ""
#         substring = s[l]
        
#         for r in range(1, len(s)):
#             substring += s[r]
#             #print("current substring: ", substring)
#             if s[r] != s[l]:
#                 #print("if substring: ", substring)
#                 continue
#             else: 
#                 #print("else substring: ", substring)
#                 if substring == substring[::-1] and len(substring) > len(result):
#                     result = substring
#                 l += 1
            
#         return result

        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # for odd-length strings
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
            # for even-length strings
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1   
                l -= 1
                r += 1
                
        return res
                    
        