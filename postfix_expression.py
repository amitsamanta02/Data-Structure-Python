OPERATOR = ['*','+','-','/',"%"]
POST_FIX = ['10','3','5','*','16','4','-','/','+']
max_size = 50

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
    for ele in POST_FIX:

        if ele == '+':
            val1 = st.pop()
            val2 = st.pop()
            val = int(val2) + int(val1)
            st.push(val)
            continue
        elif ele == '-':
            val1 = int(st.pop())
            val2 = int(st.pop())
            val =  val2 - val1
            st.push(val)
            continue
        elif ele == '*':
            val = int(st.pop()) * int(st.pop())
            st.push(val)
            continue
        elif ele == '/':
            val1 = int(st.pop())
            val2 = int(st.pop())
            val = val2 - val1
            st.push(val)
            continue
        else:
            st.push(ele)


    final = st.pop()
    print(final)




