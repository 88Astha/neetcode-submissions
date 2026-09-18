class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lenn = 0
        l = 0 
        charlen = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
              
                 
            seen.add(s[r])
            lenn = max(lenn,r-l+1)

        return lenn

        

