#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        if (l < 1 or r > 32):
            return x
        ''' x=44, y=3, l=1, r=5 
            44 = 101100
             3 = 000011
        '''
        masklen=r-l+1       # 5-1+1=5
        mask=1<<masklen     # 000001 -->> 100000
        mask=mask-1         # 011111
        mask=mask<<(l-1)    # push left to bring to position ( not neeeded in this case )
        mask=mask&y         # 000011
        ans=x|mask          # 101111
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends


'''

Example 1:

Input: 
X = 44, Y = 3 
L = 1,  R = 5
Output: 47
Explaination: presenation of 44 and 3 are 
101100 and 11. So in the range 1 to 5 there 
are two set bits. If those are set in 44 
it will become 101111 = 47.

Example 2:

Input: 
X = 16, Y = 2
L = 1,  R = 3
Output: 18
Explaination: representation of 16 and 2 
are 10000 and 10. If the mentioned rule is 
followed then 16 will become 10010 = 18.

'''
