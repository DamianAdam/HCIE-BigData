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
