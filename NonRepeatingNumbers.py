#User function Template for python3

class Solution:
    def singleNumber(self, nums):
        xorOfAll=nums[0]
        for i in range(1, len(nums)):
            xorOfAll=xorOfAll^nums[i]
        rightmostSetBit = xorOfAll&~(xorOfAll-1) # bcuz for rightmost set bit to be 1 after xor, other elements should have 0 at that position
        x,y=0,0
        for i in nums:
            if( rightmostSetBit & i ):
                x=x^i
            else:
                y=y^i
        arr=[]
        arr.append(x)
        arr.append(y)
        arr=sorted(arr)
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split()))
        ob = Solution();
        ans = ob.singleNumber(v)
        for i in ans:
            print(i, end = " ")
        print()

# } Driver Code Ends


'''

Example 1:

Input: 
N = 2
arr[] = {1, 2, 3, 2, 1, 4}
Output:
3 4 
Explanation:
3 and 4 occur exactly once.
Example 2:

Input:
N = 1
arr[] = {2, 1, 3, 2}
Output:
1 3
Explanation:
1 3 occur exactly once.

'''
