class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        sum1=0 
        for i in range(0,len(nums)-1): 
            st=i+1 
            end=len(nums)-1
            while st<end:
                s=nums[st]+nums[i]+nums[end] 
                if s == target:
                    return target
                elif abs(s-target)<res:
                    res=abs(s-target)
                    sum1=s
                if s < target:
                    st+=1
                else:
                    end-=1
        return sum1