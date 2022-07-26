class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the strings: anagrams will have same output strings
        # remember their initial positions (needed?)
        # group them together in new array of arrays
        
        dict = {}
        sorted_strs = [""] * len(strs)
        
        for i in range(len(strs)):
            sorted_strs[i] = ''.join(sorted(strs[i])) # sort characters in anagram alphabetically: str > list > str
            #print(sorted_strs[i])
            if sorted_strs[i] not in dict:
                dict[sorted_strs[i]] = [i]
            elif sorted_strs[i] in dict:
                dict[sorted_strs[i]].append(i)
                
            #print("dict: ", dict)
            
        result = []
            
        for value in dict.values():
            grouped = []
            #print(grouped)
            for element in value:
                #print(strs[element])
                grouped.append(strs[element])
            #print(grouped)
            result.append(grouped)
            
                       
        return result
            
        
        
        
        
        
        