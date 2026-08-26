class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_array=[None] * len(nums) * 2
        for index in range(len(ans_array)):
            if index < len(nums):
                calculated_index = index
            else:
                calculated_index = index - len(nums)
            ans_array[index] = nums[calculated_index]
        return ans_array
        