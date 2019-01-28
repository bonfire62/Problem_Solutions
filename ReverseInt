# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output: 321
# Example 2:
# 
# Input: -123
# Output: -321
# Example 3:
# 
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

##
#Solution 70% faster than total submissions
##

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rtype = ''
        a = str(x)
        negcheck = False
        if(a[0] == '-'):
            negcheck = True
            a = int(a[1:len(a)])
        a = int(a)
        while(a>=10):
            x = a%10
            rtype += str(x)
            a = a//10
        rtype += str(a)
        if(int(rtype) > 2**31):
            return 0
        else:
            if(negcheck):
                return int('-' + rtype)
            else:
                return int(rtype)

sol = Solution()


print(sol.reverse(1534236469))
print(sol.reverse(123))
