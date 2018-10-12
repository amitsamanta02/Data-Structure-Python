class Node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = next

class queue1(object):
    head = None
    tail = None

    def enqueue(self,ele):
        node = Node(ele,None)
        if self.head == None:
            self.head = node
            node.next = None
            self.tail = node
        else:
            self.tail.next = node
            node.next = None
            self.tail = node

    def dequeue(self):
        if self.head == None:
            print("Queue is empty!!")
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp


if __name__ == '__main__':
    q = queue1()
    q.dequeue()
    q.enqueue(10)
    val = q.dequeue()
    print(val)
    q.enqueue(10)
    q.enqueue(20)
    val2 = q.dequeue()
    print(val2)
    val2 = q.dequeue()
    print(val2)
    val2 = q.dequeue()
    print(val2)