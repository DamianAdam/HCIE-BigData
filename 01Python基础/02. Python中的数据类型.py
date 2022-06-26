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

""" 知识点二：字符串类型 """
