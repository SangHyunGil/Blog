import sys
from itertools import permutations, takewhile
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SingleLinkedList():
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0
        self.tail = Node("dummy")
        self.head.next = self.tail
        self.tail.prev = self.head

    def sizes(self):
        return self.size

    def isEmpty(self):
        return False if self.size else True
    
    def find(self, idx):
        if self.size == 0 or idx >= self.size :
            return IndexError
        else:
            if (self.size - idx) > idx:
                store = self.head
                for i in range(idx):
                    store = store.next

            else:
                store = self.tail
                for i in range(idx):
                    store = store.prev

            return store

    def appendleft(self, data):
        newNode = Node(data)
        store = self.head.next
        # head와 양방향 연결
        self.head.next = newNode
        newNode.prev = self.head
        # next node와 양방향 연결
        store.prev = newNode
        newNode.next = store
        
        self.size += 1

    def append(self, data):
        newNode = Node(data)
        store = self.tail.prev
        # tail과 양방향 연결
        newNode.next = self.tail
        self.tail.prev = newNode
        # prev node와 양방향 연결
        store.next = newNode
        newNode.prev = store
        
        self.size += 1

    def insert(self, idx, data):
        if idx >= self.size:
            return IndexError
        else:
            newNode = Node(data)
            if (self.size - idx) > idx:
                store = self.head
                for i in range(idx):
                    store = store.next

            else:
                store = self.tail
                for i in range(self.size-idx+1):
                    store = store.prev

            temp = store.next
            # 중간에 양방향 연결
            store.next = newNode
            newNode.prev = store
            newNode.next = temp
            temp.prev = newNode


    def delete(self, idx):
        if self.size == 0 or idx >= self.size:
            return IndexError
        else:
            if (self.size - idx) > idx:
                store = self.head
                for i in range(idx):
                    store = store.next

            else:
                store = self.tail
                for i in range(idx):
                    store = store.prev

            temp = store.next.next
            store.next = temp
            temp.prev = store

            self.size -= 1

    def __str__(self):
        s = ""
        store = self.head.next
        while store.next:
            s += str(store.data) + " -> "
            store = store.next
        s += str(store.data)
        return s
    
# Single LinkedList Insert Test
link = SingleLinkedList()
for i in range(4):
    link.append(i)

print("SingleLinkedList Print :", link) # LinkedList 출력
link.insert(3, 5) # LinkedList 삽입
print("SingleLinkedList Print :", link) # LinkedList 출력
print("SingleLinkedList Size :", link.sizes()) # LinkedList 사이즈
print("SingleLinkedList isEmpty :", link.isEmpty()) # LinkedList Empty 확인
print()

# Single LinkedList Delete Test
link.delete(1) # LinkedList 
print("SingleLinkedList Print :", link)
print("SingleLinkedList Size :", link.sizes())