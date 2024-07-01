class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num={}
        # for i in range(len(nums)):
        #     complement=target-nums[i]
        #     if complement in num:
        #         return [num[complement],i]
        #     num[nums[i]]=i
        # return []


        num = {}
        n=len(nums)
        for i in range(n):
            num[nums[i]]=i
        for i in range(n):
            c=target-nums[i]
            if(c in num and num[c]!=i):
                return [num[c],i]
        return []