"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res,count,res=0,0,0
        i,j=0,0
        while i <len(intervals) or j<len(intervals):
            if i<len(intervals) and start[i]<end[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res = max(res,count)
        return res

        
