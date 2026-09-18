class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = {}
        
        for char in s1:
            count[char] = count.get(char,0) + 1

        l = 0
        windowcount = {}
        for r in range(len(s2)):
            windowcount[s2[r]] = windowcount.get(s2[r],0) + 1

            

            while (r - l + 1) > len(s1):
                windowcount[s2[l]] -= 1
                if windowcount[s2[l]] == 0:
                    del windowcount[s2[l]]
                l += 1

            if count == windowcount:
                return True
            
            

        return False



