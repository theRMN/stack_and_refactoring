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
ts = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']


def check_balance(item):
    for i in item:
        if i in ['[', '(', '{']:
            fst.push(i)
        elif not fst.isEmpty() and fst.peek() + i in ['()', '{}', '[]']:
            fst.pop()
        else:
            return print('Не сбалансировано')

    if fst.isEmpty():
        return print('Сбалансировано')
    else:
        return print('Не сбалансировано')


if __name__ == '__main__':
    for it in ts:
        check_balance(it)
