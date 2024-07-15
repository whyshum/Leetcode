class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h==len(piles):
        #     return max(piles)
        # st,end=1,max(piles)
        # res=end
        # while st<=end:
        #     mid=(st+end)//2
        #     ct=0
        #     for i in piles:
        #         ct+= math.ceil(i/mid)
        #     if(ct<=h):
        #         res=min(res,mid)
        #         end=mid-1
        #     else:
        #         st=mid+1
        # return res
        st,end=ceil(sum(piles)/h),max(piles)
        res= end
        while(st<=end):
            mid=(st+end)//2
            ct=0
            for i in piles:
                ct+=ceil(i/mid)
            if ct>h:
                st=mid+1
            else:
                res=mid
                end=mid-1
        return res
                