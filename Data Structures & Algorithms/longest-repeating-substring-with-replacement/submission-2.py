class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxlen = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            while ((r - l + 1) - max(count.values()) > k):
              
                count[s[l]] -= 1
                l += 1
            
            
            maxlen = max(maxlen,r - l + 1)
        return maxlen
