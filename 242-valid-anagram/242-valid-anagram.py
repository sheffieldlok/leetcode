class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0 or len(t) != len(s): return False
        
        # 1. Put s into a dictionary, key = letter, value = # of times letter appears
        # 2. Compare t with s letter by letter:
        #   2.1 if letter in t exists in dict: update k,v pair, value--
        #   2.2 if letter in t does not exist: return false
        # 3. if dictionary is empty, return true. else return false.
        
        dict = {}
        
        for i in range(len(s)):
            if s[i] in dict: # if letter exists in dictionary already
                dict[s[i]] += 1
            else:   # new letter that is not in dict
                dict[s[i]] = 1
            
        for i in range(len(t)):
            if t[i] in dict:
                dict[t[i]] -= 1
                if dict[t[i]] == 0:
                    del dict[t[i]]
            else: 
                return False
            
        if dict == {}: return True
        else: return False
        
                    
        
        
        
        