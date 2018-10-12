max_size = 5
class Stack(object):
    def __init__(self):
        self.data = []

    def push(self,ele):
        if len(self.data) == max_size:
            print("stack is Full")
        else:
            self.data.append(ele)

    def pop(self):
        if len(self.data) == 0:
            print("stack is empty")
            return
        else:
            temp = self.data[len(self.data) - 1]
            del self.data[len(self.data)-1]
            return temp

if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)
    st.push(60)
    ele = st.pop()
    print("poped element =: ",ele)
    ele = st.pop()
    print("poped element =: ", ele)
    ele = st.pop()
    print("poped element =: ", ele)
    ele = st.pop()
    print("poped element =: ", ele)
    ele = st.pop()
    print("poped element =: ", ele)
    ele = st.pop()
    print("poped element =: ", ele)





