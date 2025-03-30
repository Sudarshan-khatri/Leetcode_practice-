class Solution:
    def insertion_sort(self,num):
        for i in range(len(num)-1):
            least=num[i]
            p=i
            for j in range(len(num)-1):
                if(num[j]<least):
                    least=num[j]
                    p=j

            num[least],num[i]=num[i],p

        return num
    

# instance of class
obj1=Solution()
arr=[2,8,5,2,8,3,8,3,6,9,4,2,5,8,77]
print(obj1.insertion_sort(arr))