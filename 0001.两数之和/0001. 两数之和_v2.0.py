'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
'''
'''
与第一版相比，删掉了内层循环
创建空列表，不在的加入，在的输出：这个就是所谓的hash map？
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = []
        for i in range(len(nums)):
            if (target - nums[i]) not in find:
                find.append(nums[i])
            else:
                return find.index(target - nums[i]), i