class Stack(object):

    def __init__(self,data,next):
        self.data = data
        self.next = next


class stackop(object):
    top = None

    def push(self,ele):
        head = None
        st = Stack(ele,None)
        if self.top == None:
            self.top = st
            head = st
        else:
            head = self.top
            self.top.next = st
            self.top = st
        print(st.data)

    def pop(self):
        top1 = self.top
        if top1 == None:
            print("STack is empty")
            return(None)
        else:
            r = top1.data
            top1.next = None
            self.top = self.top1
            print(r)


if __name__ == "__main__":
    sat = stackop()
    sat.pop()
    sat.push(10)
    sat.push(20)
    sat.push(30)
    sat.pop()
    sat.pop()




