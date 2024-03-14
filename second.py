import random

# Функция для сохранения словаря в файл
def save_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write(f'{key}: {value}\n')

# Функция для получения списка имен от пользователей
def get_names():
    names_list = []
    print("Введите имена участников (введите 'стоп' для завершения ввода):")
    while True:
        name = input("Введите имя: ").strip()
        if name.lower() == 'стоп':
            break
        elif name and name not in names_list:
            names_list.append(name)
        else:
            print("Имя не может быть пустым или повторяться.")
    return names_list

names_list = get_names()
names_dict = {i+1: name for i, name in enumerate(names_list)}

# Сохраняем словарь в файл
save_dict_to_file(names_dict, 'santa_numbers.txt')
print("Словарь дарителей сохранён в файле 'santa_numbers.txt'.")

# Создаем отдельный список для получателей
receivers_list = names_list[:]

# Перемешиваем список получателей
random.shuffle(receivers_list)

# Мы будем повторять процесс, пока не назначим каждому дарителю получателя
for santa_num, santa_name in names_dict.items():
    # Выбираем первого получателя из списка
    receiver_name = receivers_list.pop(0)
    print(f'{santa_num}, ты даришь подарок {receiver_name}')
