#-*-coding:utf-8-*-
#'''
#    单向链表的实现
#    1.node
#        value
#        next
#    2.llist
#        append
#        prepend
#        len
#        inset
#    
#'''

class Node():
    def __init__(self,value=None,next=None):
        self.value,self.next=value,next
        
    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)
        
    __repr__= __str__
    
class FullException(Exception):pass

class Llist():
#    '''
#    头节点
#    '''
    def __init__(self,maxsize_):
        self._rootnode = Node()
#        self._rootnode.next=self._rootnode
        self._length = 0
        self._maxsize = maxsize_
        self._tailnode = None
    def __len__(self):
        return self._length
    
#    def append(self,value_):
#        if self._length+1>=10:raise FullException
#        self._tailnode = Node(value_)
#        if self._rootnode.next == None:
#            self._rootnode.next = self._tailnode
#        else:
#            cnode = self._rootnode
#            while cnode.next is not None:
#                cnode = cnode.next
#            lastnode = cnode
#            lastnode.next = self._tailnode
#        self._length +=1
    def append(self,value):
        if self._maxsize is not None and self._length>=self._maxsize:
            raise FullException
        newnode = Node(value)
        if self._tailnode is None:#never added node
#            self._rootnode.next = self._tailnode
            self._rootnode.next = newnode
        else:
            self._tailnode.next = newnode
        self._tailnode = newnode
        print('add %d'%value)
        self._length +=1
        
    def appendleft(self,value):
        if self._maxsize is not None and self._length>=self._maxsize:
            raise FullException
        if self._length == 0:self.append(value)
        else:
            firstnode = self._rootnode.next
            newnode = Node(value)
            self._rootnode.next = newnode
            newnode.next = firstnode
        self._length +=1
    
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
            
    def iter_node(self):
        startnode = self._rootnode.next
        while startnode is not self._tailnode:
            yield startnode
            startnode = startnode.next
        yield startnode
    def remove(self,value_):
        prenode = self._rootnode
        curnode = self._rootnode.next
        for curnode in self.iter_node():
            if curnode.value == value_:
                prenode.next = curnode.next
                del curnode
                self.length -=1
                return 0
            prenode = curnode
        return -1
    def find(self,value_):
        prenode = self._rootnode
        curnode = self._rootnode.next
        for curnode in self.iter_node():
            if curnode.value == value_:
                prenode.next = curnode.next
                return curnode
            prenode = curnode
        return None
if __name__ == '__main__':
    t = Llist(maxsize_=12)
    for i in range(5):
        print(i)
    t.append(1)
    t.append(2)
    t.append(5)
    print(t)
    print(t.find(5))
    pass
#    def __iter__(self):
#        curnode = self.rootnode
#        nextnode = curnode.next
#        if nextnode !=self.rootnode:
#            yield curnode
#            
#    def append(self,value):
#        newnode=Node(value)
#        if self.length ==0:
#            self.rootnode.next=newnode
#            newnode.next = self.rootnode
#        else:
            