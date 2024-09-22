queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
storage = {}  #создаю пустой словарь

for query in queries:
    words = query.split() #разбиваю на строки

    if len(words) in storage.keys():  #получить ключ(storage.keys) по длине строки
        storage[len(words)] += 1  #добавляем 1 к каждому индексу в множестве storage
    else:
        storage.update({   #обновляю/дополняю словарь
            len(words): 1
        })

for key, value in storage.items(): #получить ключи и значения
    percentage = round((value / len(queries)) * 100, 1) # round() округляет число до той цифры, что я задала
    print(f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)')