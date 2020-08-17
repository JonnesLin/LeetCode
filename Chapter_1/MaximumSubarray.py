class Solution(object):
    def __init__(self, flag=True):
        self.flag = flag
    """
    使用动态规划解决
    心路历程:想了想，我们只要遍历一次数组，然后看看加上一个数之后会不会比没加的结果大。
    通式: result = max(before_result, before_result_added_current_element)
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if self.flag:
            # 设置用于存储
            saved_data = [0]
            if len(nums) == 0:
                return 0
            for index in range(len(nums)):
                saved_data.append(max(nums[index] + saved_data[index], nums[index]))
            return max(saved_data[1:])


if __name__ == '__main__':
    solution = Solution(True)
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(array))