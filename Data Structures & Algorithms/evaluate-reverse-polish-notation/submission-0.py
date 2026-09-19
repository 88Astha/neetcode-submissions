class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        def calc(op,a,b):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return int(a / b)
                
        ans = 0 
        for i in tokens:
            if i in "+-*/":
                second = stk.pop()
                first = stk.pop()
                ans = calc(i,first,second)
                stk.append(ans)

            else:
                stk.append(int(i))

        return stk[0]