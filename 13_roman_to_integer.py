class Solution:
    def romanToInt(self, y: str) -> int:
        a={
         'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
          }
        r=0
        for i in range(len(y)):
            if i+1 < len(y) and a[y[i+1]] > a[y[i]]:
                r-=a[y[i]]
            else:
                 r+=a[y[i]]
        return r
