import random

names_list = ['Ann', 'Jenya', 'Natalya', 'Dima', 'Alexandr', 'Andrey']
names_dict = {i+1: name for i, name in enumerate(names_list)}
names_dict_str = ', '.join([f'{num}: {name}' for num, name in names_dict.items()])

print("Список дарителей и их номера:")
print(names_dict_str)

# Создаем отдельный список для получателей
receivers_list = names_list[:]

# Перемешиваем список получателей
random.shuffle(receivers_list)

# Мы будем повторять процесс, пока не назначим каждому дарителю получателя
for santa_num, santa_name in names_dict.items():
    # Выбираем первого получателя из списка
    receiver_name = receivers_list.pop(0)
    print(f'{santa_num}, ты даришь подарок {receiver_name}')
