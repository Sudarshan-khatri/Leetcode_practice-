import math


class Solution:
    def mySqrt(self, x: int) -> int:
        root=math.sqrt(x)
        return int(root)



#crete an instance of the class
obj_1=Solution()
print(obj_1.mySqrt(4))
print(obj_1.mySqrt(8))
        