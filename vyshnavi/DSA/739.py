class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans=[0]*len(temperatures)
        # st=[]
        # for i,v in enumerate(temperatures):
        #     while st and st[-1][1]<v:
        #         index,value=st.pop()
        #         ans[index]=i-index
        #     st.append([i,v])    
        # return ans
        result = [0] * len(temperatures)
        st = []
        for i, val in enumerate(temperatures):
            while st and val > temperatures[st[-1]]:
                result[st.pop()] = i - st[-1]
            st.append(i)
        return result