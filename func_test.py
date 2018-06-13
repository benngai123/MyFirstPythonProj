a = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x > 2, a)))

c = list(map(lambda x: x + 1, a))
print(c)
b = [5, 7, 9]
d = list(map(lambda x, y: x + y, a, b))
print(d)

# reduce
from functools import reduce

z = reduce(lambda x, y: x + y, [2, 3, 4])
print(z)

# zip
a = (1, 2, 3)
b = (4, 5, 6)
for i in zip(a, b):
    print(i)

# key:value 对调
dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))
