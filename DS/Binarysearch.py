"""Binary search in the way of half way"""
class BinarySearch():
    def Binary(self,num,key):
        lowest=0
        highest=len(num)-1
        while lowest<=highest:
            mid=(lowest+highest)//2
            if num[mid]<key:
                highest=mid-1
            elif num[mid]>key:
                lowest=mid+1
            else:
                return f'Position:{mid+1} and value:{num[mid]}'
        return 'key not found'

#instnce of class :
num=[9,8,7,6,5,4,3,2,1]
obj1=BinarySearch()
print(obj1.Binary(num,3))