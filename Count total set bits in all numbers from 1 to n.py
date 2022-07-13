#User function Template for python3

class Solution:
    
    dp={}
        
    def findMSB(self, x):
        i=0
        while(pow(2, i)<=x):
            i+=1
        return i-1
 
    def countSetBits(self, n):
     
        if (n <= 1):
            return n
        elif n in self.dp:
            return self.dp[n]
        x = self.findMSB(n)
        self.dp[n]=(x * pow(2, (x))//2 ) + (n - pow(2, x) + 1) + self.countSetBits(n - pow(2, x))
        # before 8, there are 3 columns with 4 1's, 8's msb is at 3, so (3*8//2) -->> 3*(2^3)//2 ( 8 is 2^3 )
        return self.dp[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends

'''

Example 1:

Input: N = 4
Output: 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bits
For 2: 0 1 0 = 1 set bits
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bits
Therefore, the total set bits is 5.
Example 2:

Input: N = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), 
the total number of set bits is 35.

'''
