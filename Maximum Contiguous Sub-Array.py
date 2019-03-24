# This solution utilizes Kadanes algorithm. This is based on dynamic programming. The algorithm makes use of the fact that we can 
# dynamically keep track of the maximum sub-array at this location. the currSum compares the max of the previous sub-array at it's current
# index, with the next number. *This determines if it is adventageous to start a new array, or to continue the previous sub array*. maxSum
# simply keeps track of the maximum sum. 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum
