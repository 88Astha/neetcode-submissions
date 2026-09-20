class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) - 1

        l  = 0
        r = m

        col = -1

        for i in range(n):
            if target >= matrix[i][0] and target <= matrix[i][m]:
                col = i
                break

        if col == -1:
            return False


        while l <= r:
            mid = (l + r) // 2
            if matrix[col][mid] == target:
                return True
            elif matrix[col][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
            