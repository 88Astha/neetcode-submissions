class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = need = 0

        res, reslen = [-1,-1] , float('inf')

        count = {}
        for it in t:
            count[it] = 1 + count.get(it,0)

        need = len(count)

        l = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r],0) + 1

            if s[r] in count and counts[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    res = [l,r]
                    reslen  = r - l + 1

                popchar = s[l]
                counts[s[l]] -= 1

                if popchar in count and counts[s[l]] < count[s[l]]:
                    have -= 1
               
                l += 1

            
        l , r = res
        return s[l : r+1] if reslen != float('inf') else ""

            
