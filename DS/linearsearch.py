"""Linear search to find the given valuer"""
class LinearSearch():
    def Cards(self,num,key):
        for i in range(0,len(num)-1):
            if num[i]==key:
                return i
                break
          
        return f"Not found"
            

#instance of class linearSearch
nums=[]
key=4
obj1=LinearSearch()
print(obj1.Cards(nums,key))