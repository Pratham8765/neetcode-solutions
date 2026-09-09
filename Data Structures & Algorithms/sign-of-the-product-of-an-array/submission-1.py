class Solution:
    
    def signFunc(self,x:int)->int:
        if x<0:
            return -1
        elif x>0:
            return 1
        return 0
    def arraySign(self, nums: List[int]) -> int:
        for i in nums:
            if i==0:
                return 0
        prod=1
        for num in nums:
            prod=prod*num
        return self.signFunc(prod)
