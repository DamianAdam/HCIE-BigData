""" 分支结构 """
age = 20
if age < 18:
    print("未成年")
elif age == 18:
    print("刚成年")
else:
    print("已成年")

""" while循环 """
# 计算n的阶乘
n = eval(input("Enter n: "))
result = i = 1
while i <= n:
    result *= i
    i += 1
print(result)

# while True:
#     print("Hello World")

n = 1
while n <= 10:
    print(n)
    n += 1
else:
    print("循环结束")

""" for循环 """
# 迭代range对象。
for i in range(1, 100):
    print(i)

# 迭代列表。
lst = [1, 3.1, True, "ABC"]
for i in lst:
    print(i)

for i in range(1, 10):
    print(i)
else:
    print("Hello Python")

""" pass关键字 """
for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)

""" break关键字 """
for i in range(1, 11):
    for j in range(1, 11):
        if i == 5:
            break
        print(i, end="\t")
    print()

""" continue关键字 """
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)