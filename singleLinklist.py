class Node():

    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linklist():

    head=None
    tail=None

    def insert(self,data):
        node = Node(data,None)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def show(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
        print(None)

    def delete(self,ele):
        current_node = self.head
        prev = None
        while current_node != None:
            if current_node.data == ele:
                if prev == None:
                    self.head = current_node.next
                else:
                    prev.next = current_node.next
            prev = current_node
            current_node = current_node.next


if __name__ == "__main__":
    l = Linklist()
    l.insert(10)
    l.insert(20)
    l.insert(30)
    l.insert(40)
    l.show()
    l.delete(40)
    l.show()



