'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。
 

示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0
'''
'''
这题提交了好多次都败了，要考虑仔细
实际上就是分成三部分，左边升序，右边升序，中间乱序，但是要考虑左边最大值和右边最小值以及中间值的关系
累了，找了个题解近乎于抄出来了
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while r>=1 and nums[r-1]<=nums[r]:
            r -= 1
        if r == 0:
            return 0
        maxi = max(nums[:r+1])
        while r<n-1 and nums[r+1]<maxi:
            r += 1
        while l<n-1 and nums[l+1]>=nums[l]:
            l += 1
        mini = min(nums[l:])
        while l>0 and nums[l-1]>mini:
            l -= 1
        return r - l + 1