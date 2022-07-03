def f(x):
    """
    计算参数x的平方
    :param x: 数值类型
    :return: x的平方
    """
    result = x ** 2
    return result


f10 = f(10)
print(f10)  # 100


def sum(num1, num2):
    return num1 + num2


print(sum(10, 23))  # 33
print(sum(num2=132, num1=423))  # 555


def fuc(num1, num2, num3=100):
    return num1 + num2 + num3


print(fuc(100, 200, 300))
print(fuc(100, 200))


def fun(a, b, c=100, *args, **kwargs):
    print(a, b, c)
    print(type(args), args)
    print(type(kwargs), kwargs)


fun(1, 2, 3, 4, 5, 6, 7, k1="v1", k2="v2")

def func(a, b, c=100, d=200, *args, **kwargs):
    pass
