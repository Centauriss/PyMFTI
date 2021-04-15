HELP = """ Доступные команды:
* help - напечатать справку
* add - добавить задачу
* exit - выход из программы
* print - напечатать все задаыи 
"""
# tasks = []
# today = []
# tomorrow = []
# other = []
todos = dict()

stop = False
# MAX_ATTEMPS = 10
# attemp = 0

while not stop:
    command = input('Введите команду: \n')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date in todos:
            todos[date].append(task)
        else:
            todos[date] = [task]
        print(f'Задача {task} добавлена на {date}')
        # elif date == 'tomorrow':
        #     tomorrow.append(task)
        #     print(f'Задача {task} добавлена')
        # else:
        #     other.append(task)
        # print(f'Задача {task} добавлена')
    elif command == 'print':
        date = input('Введите дату: ')
        if date in todos:
            for task in todos[date]:
                print(task)
        else:
            print(f'По дате {date} нет задач')
    elif command == 'exit':
        stop = True
    else:
        print('Неизвестная команда')
        stop = True
    # attemp += 1
    # print('attemp', attemp)

# print('today', today)
# print('tomorrow', tomorrow)
# print('other', other)

# for task in today:
#     print(task)
# for task in tomorrow:
#     print(task)
# for task in other:
#     print(task)

print("The END. Спасибо за использование")
