import random
import unittest

# Функция для сохранения словаря в файл
def save_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write(f'{key}: {value}\n')

# Функция для создания словаря дарителей
def create_santa_dict(names_list):
    return {i+1: name for i, name in enumerate(names_list)}

# Функция для создания пар "даритель-получатель"
def assign_santas(names_list):
    receivers_list = names_list[:]
    random.shuffle(receivers_list)
    pairs = {}
    for santa_num, santa_name in enumerate(names_list, start=1):
        for receiver_name in receivers_list:
            if santa_name != receiver_name:
                pairs[santa_num] = receiver_name
                receivers_list.remove(receiver_name)
                break
    return pairs

# Класс для юнит-тестов
class TestSantaProgram(unittest.TestCase):

    def test_create_santa_dict(self):
        names = ['Ann', 'Jenya', 'Natalya']
        santa_dict = create_santa_dict(names)
        self.assertEqual(santa_dict, {1: 'Ann', 2: 'Jenya', 3: 'Natalya'})

    def test_assign_santas(self):
        names = ['Ann', 'Jenya', 'Natalya']
        pairs = assign_santas(names)
        self.assertEqual(len(pairs), len(names))
        for santa_num, receiver_name in pairs.items():
            # Убедимся, что даритель не дарит подарок сам себе
            self.assertNotEqual(names[santa_num-1], receiver_name)
            # Убедимся, что каждый получает подарок только один раз
            self.assertEqual(list(pairs.values()).count(receiver_name), 1)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
