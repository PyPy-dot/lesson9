from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda it: it[0] == it[1], zip(first, second))))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8', newline='\n') as file:
            file.write(str(data_set))

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *args):
        self.words = args

    def __call__(self):
        return choice(self.words)


# Ваш класс здесь

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
