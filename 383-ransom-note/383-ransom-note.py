class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_m = {}
        
        if len(ransomNote) > len(magazine): return False
        
        for i in range(len(magazine)):
            if magazine[i] not in dict_m:
                dict_m[magazine[i]] = 1
            else:
                dict_m[magazine[i]] += 1
        
        for j in range(len(ransomNote)):
            if ransomNote[j] in dict_m:
                dict_m[ransomNote[j]] -= 1
                if dict_m[ransomNote[j]] < 0:
                    return False
            else:
                return False
        
        return True
        
        
        
        