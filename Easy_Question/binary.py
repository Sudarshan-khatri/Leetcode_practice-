class binarySearch():
    def binary_search(self,num,key):
        l,h=0,len(num)-1
        while l<=h:
            mid=(l+h)//2
            if(key<num[mid]):
                h=mid-1
            elif(key>num[mid]):
                l=mid+1
            else:
                flag=1
                break
        if(flag==1):
            return mid
        
arr=[1,2,4,6,7,8,12]
obj1=binarySearch()
print(obj1.binary_search(arr,4))