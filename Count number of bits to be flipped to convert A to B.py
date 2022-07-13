#User function Template for python3

class Solution:
    
    def setBits(self, n):
        c=0
        while(n>0):
            c+=1
            n=n&n-1 
        return c
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        x=a^b
        ans=self.setBits(x)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends


'''

Example 1:

Input: A = 10, B = 20
Output: 4
Explanation:
A  = 01010
B  = 10100
As we can see, the bits of A that need 
to be flipped are 01010. If we flip 
these bits, we get 10100, which is B.

Example 2:

Input: A = 20, B = 25
Output: 3
Explanation:
A  = 10100
B  = 11001
As we can see, the bits of A that need 
to be flipped are 10100. If we flip 
these bits, we get 11001, which is B.

'''
