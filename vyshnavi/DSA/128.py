class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        longest=0
        for num in nums:
            if num-1 not in ns:
                length=1
                while(num+length) in ns:
                    length+=1
                longest=max(longest,length)
        return longest