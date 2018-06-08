#-*-coding:utf-8-*-
#'''
#µ¥ÏòÁ´±í
#'''
class LListException(Exception):
    pass

class Node():
    def __init__(self,value_,next_):
        self.value = value_
        self.next = next_
        
class LList():
    def __init__(self,maxlength_):
        self.maxlength = maxlength_
        self.length = 0
        self.rootnode = Node(None,None)
        self.tailnode = None
        
    def getTailNode(self):
        if self.rootnode.next is not None:
            startNode = self.rootnode
            while startNode.next is not None:
                startNode = startNode.next
            return startNode
        else:
            return self.rootnode
    
    def append(self,value):
        if self.length >= self.maxlength:
            raise LListException('tomany append')
        newNode = Node(value,None)
        tailnode = self.getTailNode()
        tailnode.next = newNode
        self.tailnode = newNode
        self.length+=1
        
    def leftappend(self,value):
        if self.length >=self.maxlength:
            raise LListException('tomany leftappend')
        pass
        newNode = Node(value,None)
        if self.rootnode.next is not None:
            firstNode = self.rootnode.next
            newNode.next = firstNode
#            self.rootnode.next = newNode
        else:
            self.tailnode = newNode
#            self.rootnode.next = newNode
        self.rootnode.next = newNode
        self.length+=1
    def walklist(self):
        startNode = self.rootnode.next
        i=1
        while startNode.next is not None:
            print('nodevalue {}:{}'.format(i,startNode.value))
            startNode = startNode.next
            i +=1
        print('last node {}:{}'.format(i,self.tailnode.value))
        
    def leftpop(self):
        firstNode = self.rootnode.next
        if firstNode is None:
            raise LListException('emptylist leftpop')
        secondNode = firstNode.next
        self.rootnode.next = secondNode
        if secondNode is None:
            self.tailnode = secondNode
        self.length -=1
        return firstNode.value
    
    def pop(self):
        if self.length<=0:
            raise LListException('emptylist lpop')
        startNode = self.rootnode.next
        while startNode.next is not self.tailnode:
            startNode = startNode.next
        before_tailNode = startNode
        if self.rootnode.next == before_tailNode:
            self.tailnode = None
        else:
            self.tailnode = before_tailNode
        self.length -=1
        return before_tailNode.value
        
if __name__ == '__main__':
    ll = LList(5)
    ll.leftappend(0)
    print(ll.tailnode.value)
    ll.leftappend(1)
#    print(ll.length)
#    ll.leftappend(5)
    ll.walklist()
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
#    ll.leftappend(6)