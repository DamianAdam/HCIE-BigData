""" 变量赋值 """
lst1 = [5, 1, [7, 3]]
lst2 = lst1

print(id(lst1))  # 2058910520000
print(id(lst2))  # 2058910520000

lst2[1] = 300
print(lst1)  # [5, 300, [7, 3]]

""" 浅拷贝 """
import copy

lst1 = [5, 1, [7, 3]]
lst2 = copy.copy(lst1)

print(id(lst1), id(lst2))  # 1729082378176 1729085617728
print(id(lst1[2]), id(lst2[2]))  # 1729085600576 1729085600576

lst1[1] = 100
print(lst1, lst2)  # [5, 100, [7, 3]] [5, 1, [7, 3]]

lst1[2][1] = 400
print(lst1, lst2)  # [5, 100, [7, 400]] [5, 1, [7, 400]]

""" 深拷贝 """
import copy

lst1 = [5, 1, [7, 3]]
lst2 = copy.deepcopy(lst1)

lst1[1] = 100
lst1[2][1] = 400

print(lst1, lst2)  # [5, 100, [7, 400]] [5, 1, [7, 3]]
