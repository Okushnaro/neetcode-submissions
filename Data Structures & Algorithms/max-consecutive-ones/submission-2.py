class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        largestCounter = 0
        prevOne = False
        for index in range(len(nums)):
            if nums[index] == 1:
                prevOne = True
                counter += 1
                continue

            prevOne = False
            if counter > largestCounter:
                largestCounter = counter
                counter = 0
            counter = 0
        if counter > largestCounter:
                largestCounter = counter
        return largestCounter
        