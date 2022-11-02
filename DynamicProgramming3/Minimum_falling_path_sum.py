#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix) # assigning length of matrix
        for i in range(n-2,-1,-1):
            for j in range(n):
                if j==0:
                    matrix[i][j] += min(matrix[i+1][j],matrix[i+1][j+1]) # assigning matrix valueby finding min between i+1th and next value
                elif j==n-1:
                    matrix[i][j] += min(matrix[i+1][j],matrix[i+1][j-1]) # assigning matrix valueby finding min between i+1th and previous value
                else:
                    matrix[i][j] += min(matrix[i+1][j],matrix[i+1][j+1],matrix[i+1][j-1]) # assigning matrix valueby finding min between i+1th and next value and previous value
                    
        return min(matrix[0]) # returning min of matrix
