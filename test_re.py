import re

# p = re.compile('a')
# print(p.match('b'))


# cat
# caat
# caaat
# caaaat
# caaaaat
# p = re.compile('ca*t')
# print(p.match('caaaat'))

# .
# ^ $
# p = re.compile('cat')
# print(p.match('caaaaat'))

# p = re.compile('c[abcd]t')
# print(p.match('ct'))

# p = re.compile('cat')
# print(p.match('caaaaat'))

# ^s 空行
# .*? 不使用贪婪模式

# print(r'\nx\n')

# 2018-05-10
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# year, month, day = p.match('2018-05-10').groups()
# print(year)

# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.search('aa2018-05-10bb'))  # 搜索指定字符串


# sub('c','*','abcd')
phone = '123-456-789'  # 这是电话
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub(r'\D', '', p2)  # 替换非数字字符
print(p3)
