class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# s = Stack()
# s.push(1)
# print(s.get_stack())
# print(s.peek())
# s.push('a')
# s.push('b')
# print(s.get_stack())
# print(s.peek())