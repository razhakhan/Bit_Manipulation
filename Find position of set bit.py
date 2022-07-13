#User function Template for python3

class Solution:
    
    def isPowerofTwo(self,n):
        if(n==0):
            return False
        if(n&n-1==0):
            return True
        else:
            return False
    
    def findPosition(self, n):
        if not self.isPowerofTwo(N):
            return -1
        c=0
        while(n):
            n=n>>1
            c+=1
        return c
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends
