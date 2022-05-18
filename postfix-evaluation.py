class Stack:
    def __init__(self):  # stack 초기화
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def push(self,elem):
        self.data.append(elem)

    def pop(self):
        if self.is_empty():
            return "error"
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return "error"
        return self.data[-1]

def postfixeval(expr): # postfix 계산 
    s = Stack()
    for token in expr:
        if token in "+-*/":
            op2 = s.pop()
            op1 = s.pop()
            if token =='+':
                s.push(op1+op2)
            elif token == '-':
                s.push(op1 - op2)
            elif token == '*':
                s.push(op1 * op2)
            elif token == '/':
                s.push(op1 / op2)
            elif token == '%':
                s.push(op1 % op2)
        else:
            s.push(int(token))
    return s.pop()

expr = input()
print(postfixeval(expr)) #계산값 출력

	
