class Stack():
    def __init__(self):
       self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self,item):
        if not self.is_empty():
            return self.stack.pop(item)
        
    def peak(self):
        if not self.is_empty():
            return self.stack[::-1]
    

    #stack empty condition
    def is_empty(self):
        if len(self.stack)==0:
            return "stack empty"
        else:
            return "stack not empty"
    
    def size(self):
        return len(self.stack)
    


#instance of class:
num=[1,2,3,4,56,7,7,8]
obj1=Stack()
for n in num:
    print(obj1.push(num))
print(obj1.pop(3))
print(obj1.peak()) 
print(obj1.is_empty())
print(obj1.size())       
