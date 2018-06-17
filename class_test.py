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


# user1 = Player('tom', 100, 'master')
# user2 = Player('jerry', 90, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()

class Monster:
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def print_self(self):
        print('i am monster')


class Animals(Monster):
    def __init__(self, hp=10):
        super().__init__(hp)

    def print_self(self):
        print('i am animal')
        

class Boss(Monster):
    # boss 类怪物
    def print_self(self):
        print('i am boss')


a1 = Monster(90)
print(a1.hp)
a1.run()

a2 = Animals(50)
print(a2.hp)
a2.run()
a2.print_self()
