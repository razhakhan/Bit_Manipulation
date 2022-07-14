import sys
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max=(1<<31) # (2^31)
        sign=0
        if((dividend>=0) == (divisor>=0)):
            sign=1
        else:
            sign=-1
            
        if( (dividend<=-int_max or dividend>=int_max) and (divisor==-1 or divisor==1))  :
            if sign==1:
                return int_max-1    # 2^31-1 (given in ques (leetcode))
            else:
                return -int_max     # -2^31  ((given in ques (leetcode)))
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=0
        while(dividend-divisor>=0):
            c=0
            while( dividend - (divisor<<1<<c) >=0 ):    # a<<b is same as a*b
                c+=1
            res+=(1<<c)
            dividend-=(divisor<<c)
        if sign==1:
            return res
        else:
            return -res
            
            
            
            
'''
Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

'''
