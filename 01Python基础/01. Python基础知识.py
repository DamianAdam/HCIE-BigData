""" 知识点一：注释 """
# 单行注释一
# 单行注释二
# 单行注释三

"""
多行注释一
多行注释二
多行注释三
"""

""" 知识点二：缩进 """
# IndentationError: unexpected indent:
# a = 1
#  b = 1

result = 10
if result == 0:
    print("等于0")
elif result > 0:
    print("大于0")
else:
    print("小于0")

""" 知识点三：输入输出 """
name = input("请输入你的姓名：")
print("你好，", name, "！")

""" 知识点四：import导包 """
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave image")
plt.plot(x, y)
plt.show()

""" 知识点五：变量 """
a = 10
print(type(a), a)

a = 21.455
print(type(a), a)

a = "Food"
print(type(a), a)

a, b, c = 1, 2, 3
a, b = b, a

""" 知识点六：关键字 """
import keyword

print(keyword.kwlist)
