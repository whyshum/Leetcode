class Solution:
    def isValid(self, s: str) -> bool:
        # st=[]
        # hs={')':'(',']':'[','}':'{'}
        # if len(s) % 2 !=0:
        #     return False
        # for char in s:
        #     if char in hs.values():
        #         st.append(char)
        #     elif char in hs:
        #         if st and st[-1]==hs[char]:
        #             st.pop()
        #         else:
        #             return False
        # return len(st)==0
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0