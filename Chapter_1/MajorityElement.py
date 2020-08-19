class Solution(object):
    def majorityElement(self, nums, left_index=0, right_index=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = False
        if flag:
            dic = {}
            for element in nums:
                dic[element] = dic.get(element, 0) + 1

            time = len(nums) // 2

            for key in dic.keys():
                if time < dic[key]:
                    return key
        else:
            # 结束条件
            if left_index == right_index:
                return nums[left_index]
            # right_index = len(nums)
            mid_index = (left_index + right_index) // 2
            left_value = self.majorityElement(nums, left_index, mid_index)
            right_value = self.majorityElement(nums, mid_index+1, right_index)

            if left_value == right_value:
                return left_value

            left_count = sum(1 for i in nums if i == left_value)
            right_count = sum(1 for i in nums if i == right_value)

            if left_count > right_count:
                return left_value
            else:
                return right_value


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
