class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st=[]
        res=[]
        def backtrack(op,cl):
            if op==cl==n:
                res.append("".join(st))
            if op<n:
                st.append("(")
                backtrack(op+1,cl)
                st.pop()
            if cl<op:
                st.append(")")
                backtrack(op,cl+1)
                st.pop()
        backtrack(0,0)
        return res