'''
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
'''
'''
循环，遍历一半就够了，最后讨论一下奇数大小的中间点
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        half = int(n/2)
        sum = 0
        for i in range(half):
            sum = sum + mat[i][n-1-i] + mat[n-1-i][i] + mat[i][i] + mat[n-1-i][n-1-i]
        if n % 2 == 1:
            sum += mat[half][half]
        return sum
