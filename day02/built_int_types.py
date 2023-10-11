# 列表
list = [1, 2, 3, 4, 5, 6]
print(list)
list.pop()
colours = ["red", "blue", "green"]
print(list)
print(type(colours))
print(list[0])
list.append(1)
list.append(1)
list.append(1)
list.append(1)
list.append(1)

list.insert(1, 21)
list.extend([78, 98, 21])
list1 = ['a', 'b', ['c', 'd']]
print(list1[2][1])
print(list.count(1))
print(list)

list.remove(21)
list.reverse()
print(list)
ka = list.copy()
print(ka)
sa = ['123456789', '1234567']
print("    ")
print(len(sa[1]))

ka.clear()
print(ka)

my_list = ['a', 1, 'b', 2, 'c', 'c', 3]

my_list.remove('c')
print(my_list)

# while my_list.count('c')>0:
#     my_list.remove('c')
#
#
#
# print(my_list)

# 序列分为可变和不可变 序列 元组 字符串
# 元组 和列表 range 基本
# 元组 创建好后不可修改 处理一次性数据
# 原地修改的 都不能作用在元祖上

kas = [1,'221','211','331ws']
print(my_list[1] in kas  )

# 集合 与set 对象

