class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         tup = sorted(tuple(intervals))    
#         result = []
        
#         # if 2nd position of current element > 1st pos of next --> merge
#         for i in range(len(tup)-1):
#             if tup[i][1] > tup[i+1][0]:
#                 tup[i][1] = tup[i+1][1]
#                 result.append(list(tup[i]))
#             else:
#                 result.append(list(tup[i]))
        
#         return result
        out = []
        for i in sorted(intervals):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out