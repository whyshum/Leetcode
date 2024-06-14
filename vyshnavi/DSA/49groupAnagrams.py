class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        for w in strs:
            ana[''.join(sorted(w))].append(w)
        
        return list(ana.values())