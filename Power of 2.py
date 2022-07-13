#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        if(n==0):
            return False
        if(n&n-1==0):
            return True
        else:
            return False
            
        '''
        or simply
        return ( x & (!x & (x-1) ) )
        '''

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends


'''

Example 1:

Input: N = 1
Output: YES
Explanation:1 is equal to 2 
raised to 0 (20 = 1).
Example 2:

Input: N = 98
Output: NO
Explanation: 98 cannot be obtained
by any power of 2.

'''
