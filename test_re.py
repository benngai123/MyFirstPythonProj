import re

# p = re.compile('a')
# print(p.match('b'))


# cat
# caat
# caaat
# caaaat
# caaaaat
p = re.compile('ca*t')
print(p.match('caaaat'))
