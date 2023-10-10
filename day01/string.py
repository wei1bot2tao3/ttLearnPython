text = 1
print(text)

# text = input("请输入新的text")
# print(text)
x = y = z = 123

print("hello \" python")
print('hello " python')
# y=input("请输入y的值")
# 在字符中在插入 变量的值 f-string 用法如下
print("在字符中在插入 变量的值 f-string 用法如下:")
print(f"x是{x} y:{y} ")
var = "x" in "12x6"
var2 = "x" not in "126x"
# x在126里面
print(f"判断x在12x6里面：")
print(var)
print(var2)

x = "123" + str(y)
y = "321 "
x = (x + y) * z
print(x)
print(f"x 的长度：{len(x)}")
print(x[859:], x[860])
print(x[-1])
print(x[850:861])

# 统计子串的非重叠次数
# sub：需要搜索的子串。
# start（可选）：搜索的起始位置，默认为 0。
# end（可选）：搜索的结束位置，默认为字符串的长度。
string = "asjdaw123asdko01292019210qwioqwiwduhuqiw"
print(string.count("qw", 1, 30))

# 判断存字母或者数字 且至少一个字符  返回true

print(f"x是包含字母或者数字的字符串吗？str.isalnum(x):{str.isalnum(x)}")
print(f"y是包含字母或者数字的字符串吗？{str.isalnum(y)}")
# 所有字符串中所有字符都是字母，且至少有一个字符 返回True
abc = "abcdefg"
print(f"abc是包含字母或者数字的字符串吗？{str.isalpha(abc)}")
#  拼接
abc1 = "w12,".join(abc)
print(abc1)

#  判断开始 字母
print("xyz".startswith("x"))


