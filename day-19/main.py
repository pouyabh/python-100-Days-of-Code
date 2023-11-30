def sum(num1, num2):
    return num1+num2


def div(num1, num2):
    return num1/num2


def calcu(num1, num2, func):
    return func(num1, num2)


res = calcu(3, 5, div)
print(res)
