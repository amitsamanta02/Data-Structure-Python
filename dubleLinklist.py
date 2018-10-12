class Node(object):

    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class dublelinklist(object):
    head = None
    tail = None

    def append(self,ele):
        new_node = Node(ele,None,None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def show(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def delete(self,ele):
        current_node = self.head
        while current_node != None:
            if current_node.data == ele:
                if current_node.prev != None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = self.head

            current_node = current_node.next


if __name__ == "__main__":
    l = dublelinklist()
    for i in range(1,100,10):
        l.append(i)
    l.show()
    l.delete(61)
    l.show()

