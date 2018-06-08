class mytest:
    test=[1,2,3,4,5,5,10]
    i=0
    def __iter__(self):
        return self
    def __next__(self):
        
        currentnode = self.test[self.i]
        nextnode = self.test[self.i+1]
        if nextnode != 10:
            self.i+=1
            yield currentnode
            
print(mytest())
for i in mytest():
    print(i)
