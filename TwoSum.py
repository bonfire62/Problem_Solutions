
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
##
#Submission 21% faster than total submissions
##

nums = [3,2,4]
target = 6


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for count,num in enumerate(nums):
            # print(num)
            for nexcount in range(count+1, len(nums)):
                if(num + nums[nexcount] == target):
                    return [count, nexcount]

sol = Solution()

print(sol.twoSum(nums, target))

