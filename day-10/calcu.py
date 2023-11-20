def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mult(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


opratores = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": divide,
}

num1 = int(input('insert no 1'))

for symbol in opratores:
    print(symbol)

sym_oprator = str(input('insert above symbole'))

num2 = int(input('insert no 2'))

cal_func = opratores[sym_oprator]
answer = cal_func(num1, num2)

print(answer)
