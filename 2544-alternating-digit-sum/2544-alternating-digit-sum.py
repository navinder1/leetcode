class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x=str(n)
        s=0
        for i in range(len(x)):
            if(i&1==0):
                s+=int(x[i])
            else:
                s-=int(x[i])
        return s
        