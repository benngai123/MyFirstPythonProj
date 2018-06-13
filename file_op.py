# coding=utf-8 ##以utf-8编码储存中文字符
#   讲小说的主要任务记录到文件中
import codecs

# file1 = open('name.txt', 'w', encoding='utf-8')
# file1.write(u'诸葛亮')
# file1.close()
#
# file2 = open('name.txt', encoding='utf-8')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt', 'a', encoding='utf-8')
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())
# file4.close()
#
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('=====')

file6 = open('name.txt', encoding='utf-8')
print('当前文件指针的位置: %s' % (file6.tell()))
print('当前文件指针的读取的字符: %s' % (file6.read(1)))
print('当前文件指针的位置: %s' % (file6.tell()))
file6.seek(6, 0)
print('当前文件指针的读取的字符: %s' % (file6.read(1)))
print('当前文件指针的位置: %s' % (file6.tell()))
file6.close()