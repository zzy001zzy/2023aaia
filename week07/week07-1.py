class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<=0:
           return False
        while n > 1:
         if n % 2 != 0: # 有餘數就失敗了
                return False #失敗

         n = n // 2 # 16 //2得到8  ，數字變小

        return True     