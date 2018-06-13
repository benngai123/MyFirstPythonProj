# while True:
#     try:
#         year = int(input(''))
#         print(year)
#         break
#     except ValueError:
#         print("please input int")
#         continue

# except (ValueError, AttributeError, KeyError)

# try:
#     print(1 / 0)
# except Exception as e:
#     print('0不能做除数%s' % e)


# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')
try:
    a = open('name.txt')
except Exception as e:
    print('1')
finally:
    a.close()
