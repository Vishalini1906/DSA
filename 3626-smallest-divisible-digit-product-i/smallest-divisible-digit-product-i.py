class Solution(object):
    def smallestNumber(self, n, t):
        num=n
        while True:
            product=1
            for digit in str(num):
                product*=int(digit)
            if product%t==0:
                return num
            num+=1        