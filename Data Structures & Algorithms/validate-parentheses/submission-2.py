class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(','}':'{',']':'['}

        stk = []

        for i in s:
            if i in hmap.values():
                stk.append(i)
            elif stk:
                if stk[-1] != hmap[i]:
                    return False
                stk.pop()
            else:
                return False

            
        return True if not stk else False