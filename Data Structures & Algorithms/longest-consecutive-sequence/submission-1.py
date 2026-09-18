class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = set(nums)
        longest = 0

        for num in lcs:
            if num - 1 not in lcs:
                curr_longest = 1
                while (num + curr_longest) in lcs:
                    curr_longest += 1

                longest = max(longest,curr_longest)

        return longest

            
