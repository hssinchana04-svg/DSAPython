class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
        def __init__(self, head=None):
            self.head = head

        def insertionAtBeginning(self, value):
            temp = Node(value)
            temp.next = self.head
            self.head = temp

        def printLL(self):
            t1 = self.head
            while(t1.next != None):
                print(t1.data)
                t1 = t1.next
            print(t1.data)

obj = SinglyLinkedList()
obj.insertionAtBeginning(5)
obj.printLL()