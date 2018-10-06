class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        # enumerate()函数返回的是同时有数据和下标的对象
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))