class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            st =0
            end=len(matrix[i])-1
            if(matrix[i][st]<=target<=matrix[i][end]):
                while(st<=end):
                    mid=(st+end)//2
                    if(matrix[i][mid]==target):
                        return True
                    elif(matrix[i][mid]>target):
                        end=mid-1
                    else:
                        st=mid+1
        return False