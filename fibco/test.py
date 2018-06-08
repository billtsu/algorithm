#-*-coding:utf-8-*-
import time
#f(n)=f(n-1)+f(n-2)
def deco(func):
    mdict={}
    def _(n):
        if n in mdict:
            return mdict.get(n)
        else:
            t=func(n)
            mdict[n]=t
            return t
    return _


    
class Node(object):
    def __init__(self,pre=None,next=None,key=None,value=None):
        self.pre,self.next,self.key,self.value =pre,next,key,value
        
class DoubleList(object):
    def __init__(self):
        node = Node()
        node.pre,node.next=node,node
        self.rootnode = node
    def headnode(self):
        return self.rootnode.next
    def tailnode(self):
        return self.rootnode.pre
    def remove(self,node):
        if node is self.rootnode:
            return
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
    def append(self,node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.pre = tailnode
        node.next=self.rootnode 
        self.rootnode.pre = node
        
class LRUCache(object):
    def __init__(self,maxsize=16):
        self.maxsize = maxsize
        self.cache = {}#
        self.accesslist = DoubleList()
        ret = False
        if len(self.cache)>=self.maxsize:
            ret = True
        self.isfull =ret
    
    def __call__(self,func):
        
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:
                self.accesslist.remove(self.accesslist.headnode())
                self.accesslist.append(cachenode)
                res = cachenode.value
                return res
            else:
                value = func(n)
                if not self.isfull:
                    tailnode = self.accesslist.tailnode()
                    newnode = Node(pre=tailnode,next=self.accesslist.headnode(),key=n,value=value)
                    self.accesslist.append(newnode)
                    self.cache[n]=newnode
#                    print('append::{}::{}'.format(newnode.key,newnode.value))
                    self.isfull = len(self.cache)>=self.maxsize
                else:
                    headnode = self.accesslist.headnode()
#                    print('get headnode::{}'.format((headnode.key)))
                    self.accesslist.remove(headnode)
                    tailnode = self.accesslist.tailnode()
                    newnode = Node(pre=tailnode,next=self.accesslist.headnode(),key=n,value=value)
                    self.accesslist.append(newnode)
#                    print(self.cache)
#                    print('del ::{}'.format(headnode.key))
#                    del self.cache[headnode.key]
                return value
        return wrapper
#        node.pre = self.rootnode.pre
#        node.next = self.rootnode
#        self.rootnode.pre = node
#@deco
@LRUCache()
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


if __name__ == '__main__':
#    dl = DoubleList()
#    n0=Node(key=0)
#    n1=Node(key=1)
#    n2=Node(key=2)
#    dl.append(n0)
#    dl.append(n1)
#    dl.append(n2)
#    dl.remove(n2)
    pass
    starttime = time.time()
    for i in range(1,35):
        print(fib(i))
        
    print('costtime::{}'.format(time.time()-starttime))
#no cache 35 ==>7s
#with cache 35 ===>0.001s
