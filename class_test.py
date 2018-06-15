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
    def __init__(self, name, hp, occu):
        self.__name = name  # 属性
        self.hp = hp  # 属性
        self.occu = occu

    def print_role(self):
        print('%s: %s' % (self.__name, self.hp))

    def updateName(self, new_name):
        self.name = new_name



class Monster:
    pass


user1 = Player('tom', 100, 'master')
user2 = Player('jerry', 90, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()
