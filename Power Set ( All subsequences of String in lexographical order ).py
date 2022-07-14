#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        res=[]
        n=len(s)
        for i in range(1, pow(2,n)):
            pos=0
            temp=i
            ans=""
            while(temp>0):
                if(temp & 1):
                    ans=ans+s[pos]
                temp=temp>>1
                pos+=1
            res.append(ans)
        res=sorted(res)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()
        ob = Solution();
        ans = ob.AllPossibleStrings(s)
        for i in ans:
            print(i, end = " ");
        print()
# } Driver Code Ends

'''

Example 1:

Input : str = "abc"
Output: a ab abc ac b bc c
Explanation : There are 7 subsequences that 
can be formed from abc.
Example 2:

Input: str = "aa"
Output: a a aa
Explanation : There are 3 subsequences that 
can be formed from aa.

'''

