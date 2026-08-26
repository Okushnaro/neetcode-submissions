class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsSz = len(nums)
        ans_array=[None] * numsSz * 2
        for index in range(len(ans_array)):
            
            if index < numsSz:
                calculated_index = index
            else:
                calculated_index = index - numsSz
            ans_array[index] = nums[calculated_index]
        return ans_array
        