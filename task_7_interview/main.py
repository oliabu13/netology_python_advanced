class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, new_el):
        self.data.append(new_el)

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)


def check_string(string):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    comp_obj = Stack()

    if len(string) % 2 > 0:
        return 'Несбалансированно'

    for i, el in enumerate(string):
        if el in opening:
            comp_obj.push(el)
        elif el in closing:
            if comp_obj.is_empty():
                return 'Несбалансированно'
            elif opening.index(comp_obj.peek()) != closing.index(el):
                return 'Несбалансированно'
            else:
                comp_obj.pop()
                if comp_obj.is_empty() and i == len(string) - 1:
                    return 'Сбалансированно'


# Вариант без стека
def check(data_string):
    opening = []
    closing = []
    data_list = list(data_string)
    for el in data_list:
        if el == '(' or el == '[' or el == '{':
            opening.append(el)
        elif el == ')' or el == ']' or el == '}':
            closing.append(el)

    if len(opening) == len(closing):
        print('Сбалансировано')
    else:
        print('Не сбалансировано')


if __name__ == '__main__':
    print(check_string(input('Введите строку: ')))
