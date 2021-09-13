import sys
from itertools import permutations, takewhile
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList():
    def __init__(self):
        self.head = Node("dummy")
        self.tail = Node("dummy")
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, data):
        newNode = Node(data)
        store = self.tail.prev
        # tail과 양방향 연결
        newNode.next = self.tail
        self.tail.prev = newNode
        # prev node와 양방향 연결
        store.next = newNode
        newNode.prev = store


link = DoubleLinkedList()  
for c in input().rstrip():
    link.append(c)

cursor = link.tail
for _ in range(int(input())):
    command = input().strip().split()
    if command[0] == 'P':
        newNode = Node(command[1])
        store = cursor.prev
        newNode.next = cursor
        cursor.prev = newNode
        newNode.prev = store
        store.next = newNode

    elif command[0] == 'L':
        if cursor.prev != link.head:
            cursor = cursor.prev
        

    elif command[0] == 'D':
        if cursor != link.tail:
            cursor = cursor.next
        


    else:
        if cursor.prev != link.head:
            store = cursor.prev.prev
            store.next = cursor
            cursor.prev = store

    

answer = ""
target = link.head.next

while target != link.tail:
    answer += target.data
    target = target.next

print(answer)

#head a tail