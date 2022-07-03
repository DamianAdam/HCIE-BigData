"""
● 把字符串s = "Hello World Hello Linux Hello Hadoop"中前两个hello替换成nihao  。
● 把上一步的字符串以空格分割，赋值给lst变量。
● 把lst中最后一个成员大写、小写。
● 把lst以“-”连接成一个字符串，并赋值给str2。
"""
s = "Hello World Hello Linux Hello Hadoop"
new_str = s.replace("Hello", "NiHao", 2)
print(new_str)  # NiHao World NiHao Linux Hello Hadoop

lst = new_str.split(" ")
print(lst)  # ['NiHao', 'World', 'NiHao', 'Linux', 'Hello', 'Hadoop']

last = lst[-1]
print(last.upper())  # HADOOP
print(last.lower())  # hadoop

str2 = "-".join(lst)
print(str2)  # NiHao-World-NiHao-Linux-Hello-Hadoop

"""
● 格式化输出：
● 现有字符串：s = "name=Adam|age=21|gender=male"
● 实现输出：姓名=Adam，年龄=21，性别=male
"""
s = "name=Adam|age=21|gender=male"
data = s.split("|")
name = data[0].split("=")[1]
age = int(data[1].split("=")[1])
gender = data[2].split("=")[1]
print("姓名={0}，年龄={1}，性别={2}".format(name, age, gender))

"""
● 定义一个列表lst，成员为7、1、3、5。
● 在末尾追加'TengKe'。
● 删除第二个元素1。
● 在3的后面插入'Adam'。
● 删除元素5。
"""
lst = [7, 1, 3, 5]
lst.append("TenKe")
lst.pop(1)
lst.insert(2, "Adam")
lst.remove(5)
print(lst)  # [7, 3, 'Adam', 'TenKe']

"""
● 有如下列表lst2：5、1、7、3。
● 对列表进行降序排序。
"""
lst2 = [5, 1, 7, 3]
lst2.sort(reverse=True)
print(lst2)  # [7, 5, 3, 1]

"""
● 定义一个元组，只有一个成员100。
"""
tup = (100,)
print(type(tup), tup)  # <class 'tuple'> (100,)

"""
● 定义一个字典dic1，其中：name=Adam、age=21、gender=male。
● 获取name和city键对应的值，如果键不存在，则输出“此键不存在”。
● 添加一个键：city=Shanghai。
● 把字典dic2 = {'class':'c1', 'school':'FuDan'}中的键值对添加到dic1中
● 删除school这个键值对。
"""
dic1 = {"name": "Adam", "age": 21, "gender": "male"}
name = dic1.get("name", "此键不存在")
city = dic1.get("city", "此键不存在")
print(name, city)  # Adam 此键不存在
dic1["city"] = "Shanghai"
dic2 = {'class': 'c1', 'school': 'FuDan'}
dic1.update(dic2)
dic1.pop("school")
print(dic1)  # {'name': 'Adam', 'age': 21, 'gender': 'male', 'city': 'Shanghai', 'class': 'c1'}

"""
● 定义一个集合set1：a、b、c、d。
● 添加一个元素e，删除一个元素d。
"""
set1 = {"a", "b", "c", "d"}
set1.add("e")
set1.discard("d")
print(set1)  # {'e', 'c', 'a', 'b'}

"""
定义一个列表lst1 = [1, 2, [3, 4, 5]]，分别对该列表进行深拷贝和浅拷贝，并加以验证。
"""
import copy

lst1 = [1, 2, [3, 4, 5]]
lst2 = copy.copy(lst1)
lst3 = copy.deepcopy(lst1)

print(id(lst1) == id(lst2), id(lst1[2]) == id(lst2[2]))  # False True
print(id(lst1) == id(lst3), id(lst1[2]) == id(lst3[2]))  # False Flase

"""
● 定义函数实现斐波那契数列，需要递归和非递归方式实现两种。
● 斐波那契数列：1、1、2、3、5、……
● 解读：前两个数固定为1，第三个数开始为前两个数的和。
"""
# 递归方式
def feibo1(num):
    if num <= 2:
        return 1
    else:
        return feibo1(num - 2) + feibo1(num - 1)

# 非递归方式
def feibo2(num):
    if num > 2 and isinstance(num, int):
        result = [1, 1]
        for i in range(2, num):
            tmp = result[i - 1] + result[i - 2]
            result.append(tmp)
        return result
    else:
        return "输入的必须是一个大于2的整形数据"

print(feibo1(5))  # 5
print(feibo2(5))  # [1, 1, 2, 3, 5]

"""
● 现有两个列表：lst1 = ['col1', 'col2', 'col3', 'col4', 'col5']和lst2 = [5, 1, 7, 3, 6]。
● 需求一：把lst1和lst2结合起来，形成：[('col1', 5), ('col2', 1), ('col3', 7), ('col4', 3), ('col5', 6)]
● 需求二：按照元组的第二个成员进行排序，并取出前三个col。
"""
lst1 = ['col1', 'col2', 'col3', 'col4', 'col5']
lst2 = [5, 1, 7, 3, 6]
lst3 = list(zip(lst1, lst2))
print(lst3)
