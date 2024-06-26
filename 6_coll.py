# коллекции

# Кортеж (tuple)

# упорядоченная коллекция, неизменяемая (иммутабельная) коллекция

# создание предварительно заполненного кортежа
tpl_0 = (10, 20, 0, 3.14, "python", [1,2,3])
tpl_1 = tuple("python")

# чтение значения
val_0 = tpl_0[0]
val_0 = tpl_0[-2]

# срез кортежа
slc_0 = tpl_1[2:]
slc_0 = tpl_1[2:4]

# методы кортежа
tpl_2 = (2,1,1,0,2,3,1)

# print(tpl_2.count(3))

# print(tpl_2.index(0))


# Словарь (dict, dictionary)

# неупорядоченная, изменяемая (мутабельная) коллекция

# элемент словаря - пара "ключ-значение"

# создание пустого словаря
dict_0 = {}
dict_0 = dict()

# создание предварительно заполненного словаря
dict_1 = {5:100, 0:3.14, 'A': 20, "abc": "python", "кортеж":(1,2,3)}
# print(dict_1)

lst_0 = [(10, 20), ("key", "value"), (2, 3.14)]
dict_2 = dict(lst_0)

dict_3 = dict(name="John", a=100, b=200)

# чтение значения
val_1 = dict_1["кортеж"]
val_1 = dict_1[0]

# замена значения
dict_1["A"] = 777

# добавление пары
dict_1["B"] = "hello"
dict_1[100] = [10,20,30]

# удаление пары
del dict_1["кортеж"]

# print(dict_1)


# методы словаря

i0 = list(dict_1.items())

k0 = list(dict_1.keys())

v0 = list(dict_1.values())

print(v0)

# рассмотреть остальные методы словаря
# рассмотреть множество(set)


