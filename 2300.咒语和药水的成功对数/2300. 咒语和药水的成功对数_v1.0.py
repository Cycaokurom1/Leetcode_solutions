'''
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。

同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。

请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。

示例 1：

输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
输出：[4,0,3]
解释：
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
'''
'''
简单的双循环直接超时了，测试里面有很大很大的数组
用二分查找减少一层遍历
有一些小的增进性能的地方，比如>>1
'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            left, right = 0, m-1
            spell = spells[i]
            while left < right:
                mid = (left + right) >> 1
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1
            if potions[left] * spell >= success:
                pairs[i] = m - left
        return pairs
