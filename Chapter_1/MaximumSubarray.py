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
            # 用于存储信息
            saved_data = [0]
            # 考虑边界情况
            if len(nums) == 0:
                return 0
            # 更新存储数据
            for index in range(len(nums)):
                saved_data.append(max(nums[index] + saved_data[index], nums[index]))
            return max(saved_data[1:])
        else:
            return self.maxSubArrayByDivided(nums, 0, len(nums)-1)

    def maxSubArrayByDivided(self, nums, start_index, last_index):
        if start_index == last_index:
            return nums[start_index]

        mid_index = (start_index + last_index) // 2
        left = self.maxSubArrayByDivided(nums, start_index, mid_index)
        right = self.maxSubArrayByDivided(nums, mid_index + 1, last_index)

        max_left_value = nums[mid_index]
        left_sum = 0
        # 获取从左边开始算起的最大列表
        for index in range(mid_index, start_index-1, -1):
            left_sum += nums[index]
            max_left_value = max(left_sum, max_left_value)

        max_right_value = nums[mid_index+1]
        right_sum = 0
        # 获取从右边边开始算起的最大列表
        for index in range(mid_index+1, last_index+1):
            right_sum += nums[index]
            max_right_value = max(right_sum, max_right_value)

        center_value = max_left_value + max_right_value

        return max(center_value, left, right)





if __name__ == '__main__':
    # 当flag为True的时候，采用动态规划。当flag为False的时候，采用分治的方法
    solution = Solution(False)
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(array))