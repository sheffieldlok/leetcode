class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        dict = {}
        dict["2"] = ['a', 'b', 'c']
        dict["3"] = ['d', 'e', 'f']
        dict["4"] = ['g', 'h', 'i']
        dict["5"] = ['j', 'k', 'l']
        dict["6"] = ['m', 'n', 'o']
        dict["7"] = ['p', 'q', 'r', 's']
        dict["8"] = ['t', 'u', 'v']
        dict["9"] = ['w', 'x', 'y', 'z']
        
        
        def backtrack(i, currentStr):
            if (len(currentStr) == len(digits)):
                result.append(currentStr)
                return
            
            for c in dict[digits[i]]:
                backtrack(i+1, currentStr + c)
                
        if digits:
            backtrack(0, "")
            
        return result
                
        
        
        
        
        
        