# a * x + b = y
#
# def a_line(a, b):
#     def arg_y(x):
#         return a * x + b
#
#     return arg_y


def a_line(a, b):
    return lambda x: a * x + b


# a = 3, b = 5
# x = 10 , y = 7

line1 = a_line(3, 5)
line2 = a_line(5, 10)
y = line1(10)
print(y)
print(line1(20))
print(line2(10))
