import sys


if len(sys.argv) != 2:
    sys.exit(1)

operations_list = ['+','-','*','/']
expression = sys.argv[1]


stack = []
i = 0
while i < len(expression):
    if expression[i] == '(':
        i += 1
        new_exp = ''
        while i < len(expression) and expression[i] != ')':
            if expression[i]== '(':
                break
            new_exp += expression[i]
            i += 1
        stack.append(new_exp)
    i += 1

print(stack)





