# class Solution(object):
#     def isAnagram(self, s, t):

        #  return Counter(s) == Counter(t)


        # if (len(s)!=len(t)) or set(s)!=set(t):
        #     return False
        # h={}
        # for i in range(0,len(s)):
        #     if s[i],t[h] in h:
        #         h[s[i]]=h[s[i]]+1
        #     else:
        #         h[s[i]]=1
        # for i in range(0,len(t)):
        #     if t[i] not in h:
        #         return False
        #     else :
        #         h[t[i]]-=1
        #         if h[t[i]]== -1:
        #             return False
        # return True


        # if (len(s)!=len(t)):
        #     return False
        # h1,h2={},{}
        # for i in range(0,len(s)):
        #     h1[s[i]]=1+h1.get(s[i],0)
        #     h2[t[i]]=1+h2.get(t[i],0)
        # for c in h1:
        #     if h1[c]!=h2.get(c,0):
        #         return False
        # return True


        # return sorted(s)==sorted(t)


        # if (len(s)!=len(t)) or set(s)!=set(t):
        #     return False
        # for c in set(s):
        #     if s.count(c) != t.count(c):
        #         return False
        # return True