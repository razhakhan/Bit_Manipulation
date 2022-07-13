#User function Template for python3
class Solution:
    def setBits(self, n):
        c=0
        while(n>0):
            c+=1
            n=n&n-1 
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)




# } Driver Code Ends

"""

Given a positive integer N, print count of set bits in it. 

Example 1:

Input:
N = 6
Output:
2
Explanation:
Binary representation is '110' 
So the count of the set bit is 2.
Example 2:

Input:
8
Output:
1
Explanation:
Binary representation is '1000' 
So the count of the set bit is 1.


Algo :

6 - 0110
5 - 0101

perform AND
0100 = 4

so n&n-1 unsets the rightmost bit
do this until n becomes 0

"""
