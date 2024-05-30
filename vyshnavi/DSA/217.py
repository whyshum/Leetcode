class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # myset= set(nums)
        # if len(nums)==len(set(nums)):
        #     return False
        # else:
        #     return True
        # hash set
        hset=set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)
        