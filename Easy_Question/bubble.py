class Solution:
    def bubble_sort(self,num):
        for i in range(len(num)-1):
            for j in range(len(num)-i-1):
                if num[j]>num[j+1]:
                    num[j],num[j+1]=num[j+1],num[j]


        return num


#Instance of class 
obj1=Solution()
arr=[1,2,1,3,6,8,3,6,8,3,3,6,8]
print(obj1.bubble_sort(arr))
