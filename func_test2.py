# 闭包
def counter(first=0):
    cnt = [first]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num5 = counter(5)
num10 = counter(10)
print(num5())
print(num5())
print(num5())
print(num5())
print(num5())

print(num10())
print(num10())
print(num10())
print(num10())
print(num10())
