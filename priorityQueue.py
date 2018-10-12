class Node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = next

class pqueue(object):
    head = None
    tail = None

    def enq(self,ele):
        new_node = Node(ele,None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp.data > ele and temp.next != None:
                temp = temp.next
            if temp.next == None:
                temp.next = new_node
                new_node.next = None
                self.tail = new_node


    def deq(self):
        if self.head == None:
            print("Queue is Empty!!!!")
            return
        else:
            temp = self.head
            self.head = self.head.next
            print(temp.data)

if __name__ == '__main__':
    q = pqueue()
    q.deq()
    q.enq(5)
    q.enq(15)
    q.deq()

