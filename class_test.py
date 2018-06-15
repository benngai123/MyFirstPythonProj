# 类
# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(role_name)：
#     print('name is $s , hp is %s' % (role_name['name'], role_name['hp']))
#
# print_role(user1)
# print_role(user2)


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):
        print('%s: %s' % (self.name, self.hp))


user1 = Player('tom', 100)
user2 = Player('jerry', 90)
user1.print_role()
user2.print_role()
