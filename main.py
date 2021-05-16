class Stack:
    def __init__(self):
        self.lst = []

    def isEmpty(self):
        result = self.lst == []
        return result

    def push(self, element):
        self.lst.append(element)
        return

    def pop(self):
        result = self.lst.pop()
        return result

    def peek(self):
        result = self.lst[-1]
        return result

    def size(self):
        result = len(self.lst)
        return result


fst = Stack()

if __name__ == '__main__':
    s = '(((([{}]))))'

    for i in s:
        if i in ['[', '(', '{']:
            fst.push(i)
        else:
            if not fst.isEmpty() and fst.peek() + i in ['()', '{}', '[]']:
                fst.pop()
            else:
                print('Не сбалансировано')
                quit()

    if fst.isEmpty():
        print('Сбалансировано')
    else:
        print('Не сбалансировано')
