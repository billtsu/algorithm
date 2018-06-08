# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):   # �������� root �ڵ�Ĭ�϶��� None�����Զ�����Ĭ��ֵ
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """ ���ӱ� ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        """
        self.maxsize = maxsize
        self.root = Node()     # Ĭ�� root �ڵ�ָ�� None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):    # O(1)
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)    # ����ڵ�
        tailnode = self.tailnode
        if tailnode is None:    # ��û�� append ����length = 0�� ׷�ӵ� root ��
            self.root.next = node
        else:     # ����׷�ӵ����һ���ڵ�ĺ�ߣ����������һ���ڵ��� append �Ľڵ�
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:    # �ӵ�һ���ڵ㿪ʼ����
            yield curnode
            curnode = curnode.next    # �ƶ�����һ���ڵ�
        yield curnode

    def remove(self, value):    # O(n)
        """  value:
        """
        prevnode = self.root    #
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return 1  # ����ɾ���ɹ�
        return -1  # ����ɾ��ʧ��

    def find(self, value):    # O(n)
        """ value:
        """
        index = 0
        for node in self.iter_node():   # ���Ƕ����� __iter__������Ϳ����� for ��������
            if node.value == value:
                return index
            index += 1
        return -1    # û�ҵ�

    def popleft(self):    # O(1)
        """
        """
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    assert ll.remove(0) == 1
    assert ll.remove(3) == -1
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.appendleft(0)
    assert list(ll) == [0, 1, 2]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.clear()
    assert len(ll) == 0


if __name__ == '__main__':
    test_linked_list()