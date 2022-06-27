""" 知识点一：数值类型 """
int_num1 = 12345
print(type(int_num1), int_num1)  # <class 'int'> 12345
int_num2 = 98754091327643297036847
print(type(int_num2), int_num2)  # <class 'int'> 98754091327643297036847

if 0:
    print(True)
else:
    print(False)  # False

if 4:
    print(True)
else:
    print(False)  # True

print(False + True)  # 1，即 0 + 1 = 1

float_num = 324.1252345342632411
print(type(float_num), float_num)  # <class 'float'> 324.12523453426326

complex_num = 123 - 12j
print("123-12j的实数部分：", complex_num.real)  # 123-12j的实数部分： 123.0
print("123-12j的虚数部分：", complex_num.imag)  # 123-12j的虚数部分： -12.0

print(4 + 3)  # 7
print(4 - 3)  # 1
print(4 * 3)  # 12
print(56 / 12)  # 4.666666666666667
print(56 // 12)  # 4，注意：整除不是四舍五入，而是将小数点后的数据直接截断
print(56 % 12)  # 8
print(2 ** 4)  # 16

num1 = 213
num2 = 324.1324
result = num1 + num2
print(type(num2), num2)  # <class 'float'> 324.1324

float_number1 = 3.745
int_number1 = int(float_number1)
print(int_number1)  # 3

print(round(3.72, 2))  # 3.72
print(round(3.7276, 2))  # 3.73

number_str = '%.2f' % 3.1415926
number_float = float(number_str)
print(type(number_float), number_float)  # <class 'float'> 3.14

print(10 / 3)  # 3.3333333333333335
print('%.30f' % (10 / 3))  # 3.333333333333333481363069950021

from decimal import Decimal, getcontext

result1 = Decimal(1) / Decimal(3)
print(result1)  # 0.3333333333333333333333333333

getcontext().prec = 10  # 使用getcontext的prec空值精度
result2 = Decimal(1) / Decimal(3)
print(result2)  # 0.3333333333

""" 知识点二：字符串类型 """
str1 = "abc"
print(type(str1), str1, len(str1))  # <class 'str'> abc 3
str2 = 'a'
print(type(str2), str2, len(str2))  # <class 'str'> a 1

str3 = "Hello \n World"
print(str3)

str4 = r"Hello \n World"
print(str4)

list1 = "Hello Linux Hello Python".split(" ")
print(list1)  # ['Hello', 'Linux', 'Hello', 'Python']

get_str = "--".join(list1)
print(get_str)  # Hello--Linux--Hello--Python

string1 = "abc"
string2 = "def"
new_str = string1 + string2
print(new_str)  # abcdef

duplicate_string = "abc" * 3
print(duplicate_string)  # abcabcabc

str = "Hello"
print(str[1])  # e
print(str[-1])  # o

str = "Hello Python"
print(str[:2])  # He
print(str[3:])  # lo Python
print(str[3: 10: 3])  # lPh

str = "Hello Python Hello Linux"
print(str.replace("Hello", "Hi"))  # Hi Python Hi Linux
print(str.replace("Hello", "Hi", 1))  # Hi Python Hello Linux

str = "PyThoN"
print(str.upper())  # PYTHON
print(str.lower())  # python

name = "Adam"
age = 18
gender = "male"
salary = 150000
print("我是%s，今年%03d岁，性别：%s，月薪为%+011.2f" % (name, age, gender, salary))
print("我是{0}，今年{1:03d}岁，性别：{2}，月薪为{3:+011.2f}".format(name, age, gender, salary))

""" 知识点三：列表 """
list1 = [1, 2.43, True, "ABCD"]
print(list1)  # [1, 2.43, True, 'ABCD']

list2 = [x for x in range(1, 10)]
print(list2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[3])  # 3
print(l1[1:9:2])  # [1, 3, 5, 7]

l2 = [0, 6, 1, 3, 5, 7, 1]
print(l2.index(1))  # 2

lst1 = [5, 1, 7, 3, "Hello"]
lst1.append("World")
print(lst1)  # [5, 1, 7, 3, 'Hello', 'World']

lst1.insert(3, 100)
print(lst1)  # [5, 1, 7, 100, 3, 'Hello', 'World']

new_list = [1, 2, 3]
lst1.extend(new_list)
print(lst1)  # [5, 1, 7, 100, 3, 'Hello', 'World', 1, 2, 3]

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
new_lst = lst1 + lst2
print(new_lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([1, 2, 3] * 4)  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

list1 = [13, 514, 112, 133, 514, 343, 514, 545]
list1.pop(2)
print(list1)  # [13, 514, 133, 514, 343, 514, 545]
list1.pop()
print(list1)  # [13, 514, 133, 514, 343, 514]

list1.remove(514)
print(list1)  # [13, 133, 514, 343, 514]
list1.remove(514)
print(list1)  # [13, 133, 343, 514]

del list1[3]
print(list1)  # [13, 133, 343]

lst1 = [5, 1, 7, 3, 2, 6]
lst1.sort()
print(lst1)  # [1, 2, 3, 5, 6, 7]

lst2 = [3, 7, 1, 4, 5, 8]
lst2.sort(reverse=True)
print(lst2)  # [8, 7, 5, 4, 3, 1]

lst3 = [213, 643, True, "ABC", 132]
lst3.reverse()
print(lst3)  # [132, 'ABC', True, 643, 213]

# 取前三名的成绩
# 方式一：
records = [89, 78, 98, 56, 91, 75]
print(sorted(records, reverse=True)[:3])  # [98, 91, 89]

# 方式二：
records = [89, 78, 98, 56, 91, 75]
# 必须分开写
records.sort(reverse=True)
print(records[0:3])  # [98, 91, 89]

lst = [132, 'ABC', True, 643, 213]
print(len(lst))  # 5

lst = [5, 5, 1, 3, 2, 5]
print(lst.count(5))  # 3