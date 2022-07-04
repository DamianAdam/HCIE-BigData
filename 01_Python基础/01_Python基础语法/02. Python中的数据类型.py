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

""" 知识点四：元组类型 """
tup1 = (1, 2, 3, 4, 5)
print(tup1, type(tup1))  # (1, 2, 3, 4, 5) <class 'tuple'>

tup2 = 1, 2, 3, 4, 5
print(tup2, type(tup2))  # (1, 2, 3, 4, 5) <class 'tuple'>

t1 = (1,)
print(t1, type(t1))  # (1,) <class 'tuple'>

t2 = (1)
print(t2, type(t2))  # 1 <class 'int'>

t3 = 1,
print(t3, type(t3))  # (1,) <class 'tuple'>

# TypeError: 'tuple' object does not support item assignment
# a = (1, 2, 3)
# a[1] = 3

a = (1, [1, 0])
print(a)  # (1, [1, 0])

a[1][1] = 1
print(a)  # (1, [1, 1])

print(a[0])  # 1
print(a[1])  # [1, 1]

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6)
print(t2 * 3)  # (4, 5, 6, 4, 5, 6, 4, 5, 6)

""" 知识点五：字典类型 """
# 方式一：直接使用花括号包裹。
dic1 = {"k1": "v1", "k2": "v2", "k1": "v3"}
print(dic1)  # {'k1': 'v3', 'k2': 'v2'}

# 方式二：使用dict()函数，参数为一个包含n个(k, v)的二元组的列表或元组。
dic2 = dict([("k1", "v1"), ("k2", "v2"), ("k3", "v3")])  # 参数为列表。
print(dic2)  # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
dic3 = dict((("k1", "v1"), ("k2", "v2"), ("k3", "v3")))  # 参数为元组。
print(dic3)  # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# 方式三：使用dict()函数的可变形参
dic4 = dict(k1="v1", k2="v2", k3="v3")
print(dic4)  # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

dic = {}  # 空字典
dic["k1"] = "value1"
dic["k2"] = "value1"
print(dic)  # {'k1': 'value1', 'k2': 'value1'}
dic["k1"] = "new Value1"
print(dic)  # {'k1': 'new Value1', 'k2': 'value1'}

dic = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4", "k5": "v5"}
delete = dic.pop("k3")
print(dic, delete)  # {'k1': 'v1', 'k2': 'v2', 'k4': 'v4', 'k5': 'v5'} v3

delete = dic.popitem()
print(dic, delete)  # {'k1': 'v1', 'k2': 'v2', 'k4': 'v4'} ('k5', 'v5')

dic.clear()
print(dic)  # {}

deldic = {"k1": "v1", "k2": "v2"}
del deldic
# print(deldic)  # NameError: name 'deldic' is not defined

dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
print(dic["k1"], dic["k3"])  # v1 v3
# KeyError: 'abcd'
# print(dic["abcd"])

print(dic.get("k1", "Null"))  # v1
print(dic.get("abcd", "Null"))  # Null

print(dic.items())  # dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
print(dic.keys())  # dict_keys(['k1', 'k2', 'k3'])
print(dic.values())  # dict_values(['v1', 'v2', 'v3'])

dic1 = {"k1": "v1", "k2": "v2"}
dic2 = {"k2": "value2", "k3": "v3"}
dic1.update(dic2)
print(dic1)  # {'k1': 'v1', 'k2': 'value2', 'k3': 'v3'}

""" 知识点六：集合类型 """
set1 = {1, 1, 2, 3, 3, 5, 1}
print(set1) # {1, 2, 3, 5}，重复元素被删除了

set2 = {}
print(type(set2), set2)  # <class 'dict'> {}
set2 = set()
print(type(set2), set2)  # <class 'set'> set()

s1 = {1, 2, 3}
s1.add(5)
s1.add("abc")
s1.add(5)
print(s1)  # {1, 2, 3, 5, 'abc'}，已有的元素不会被添加

s1 = {1, 2, 3}
s2 = [4, 61, "aa"]
s3 = {"k1":"v1", "k2":"v2"}

# 方式一：
# s1.update(s2)
# print(s1)  # {1, 2, 3, 4, 'aa', 61}
# s1.update(s3)
# print(s1)  # {1, 2, 3, 4, 'k1', 'aa', 61, 'k2'}

# 方式二：
s1.update(s2, s3)
print(s1)  # {1, 2, 3, 4, 'k2', 'k1', 'aa', 61}

s1 = {1, 2, 3, 4}
s1.remove(3)
print(s1)  # {1, 2, 4}
# s1.remove(3000)  # 报错KeyError: 3000

s1 = {1, 2, 3, 4}
s1.discard(3)
print(s1)  # {1, 2, 4}
s1.discard(3000)  # 不做任何处理

s = {1, 2, 3, 4}
s.clear()
print(s)  # set()

s = {1, 2, 3, 4}
s.pop()
print(s)  # {2, 3, 4}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1 & s2
print(s3)  # {3, 4}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1 | s2
print(s3)  # {1, 2, 3, 4, 5, 6}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1 - s2
print(s3)  # {1, 2}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1 ^ s2
print(s3)  # {1, 2, 5, 6}

""" 知识点七：数据类型公共方法 """
lst = [1, 42, 54, "Abc", True]
print(len(lst))  # 5

flag = False
print(type(flag))  # <class 'bool'>

lst = [5, 1, 7, 3]
for index, tmp in enumerate(lst):
    print(index, tmp)

str = "abc"
print(id(str))  # 2432064349616

lst = [12, 321, False, "Apple", "Mac"]
print("Apple" in lst)  # True

lst = [5, 1, 7, 3]
max_num = max(lst)
min_num = min(lst)
print(min_num, max_num)  # 1 7

obj = "ABC"
print(obj)  # ABC
del obj
# print(obj)  # 报错，NameError: name 'obj' is not defined

lst1 = [1, 3, 4, 6]
lst2 = ['A', 'C', 'D', 'F']
lst3 = list(zip(lst1, lst2))
print(lst3)  # [(1, 'A'), (3, 'C'), (4, 'D'), (6, 'F')]

lst1 = [1, 3, 4, 6]
lst2 = ['A', 'C', 'D', 'F', 'G', 'H', 'Z']
lst3 = list(zip(lst1, lst2))
print(lst3)  # [(1, 'A'), (3, 'C'), (4, 'D'), (6, 'F')]

lst1 = [1, 3, 4, 6]
lst2 = ['A', 'C', 'D', 'F']
my_zip = zip(lst1, lst2)
l1, l2 = zip(*my_zip)
print(list(l1))  # [1, 3, 4, 6]
print(list(l2))  # ['A', 'C', 'D', 'F']

print(isinstance(3.14, int))  # False
print(isinstance(5, int))  # True

lst = [1, 1, 4, 5, 1, 3, 2, 1, 6, 1]
print(lst.count(1))  # 5

num = 123
str_num = str(num)
print(type(str_num), str_num)  # <class 'str'> 123

tup = (1, 2, 3, 4)
lst = list(tup)
print(type(lst), lst)  # <class 'list'> [1, 2, 3, 4]

lst = [1, 2, 3, 4]
tup = tuple(lst)
print(type(tup), tup)  # <class 'tuple'> (1, 2, 3, 4)

lst = [1, 2, 3, 1, 2, 4]
s = set(lst)
print(type(s), s)  # <class 'set'> {1, 2, 3, 4}

x_loc = ('x', 5.1)
y_loc = ('y', 31.6)
z_loc = ('z', -19.7)
loc = dict([x_loc, y_loc, z_loc])
print(type(loc), loc)  # <class 'dict'> {'x': 5.1, 'y': 31.6, 'z': -19.7}

pi = 3.14
i = int(pi)
print(i)  # 3
f = float(i)
print(f)  # 3.0