class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=[]
        for i in range(0,len(position)):
            arr.append((position[i],speed[i]))
        fleet=[]
        for i,j in sorted(arr,reverse=True):
            time=(target-i)/j
            if fleet==[]:
                fleet.append(time)
            elif fleet[-1]<time:
                fleet.append(time)
        return len(fleet)