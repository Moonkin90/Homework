import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить ученика
        2. Добавить оценку ученика по предмету
        3. Средний бал ученика по предметам
        4. Все оценки ученика по всем предметам
        5. Вывести средний балл по всем предметам по каждому ученику
        6. Вывести все оценки по всем ученикам
        7. Оценки ученика по предмету
        8. Изменить оценку ученика по предмету
        9. Удалить ученика
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить ученика')
        new_student = input('Введите имя: ')
        students.append(new_student)
        students_marks[new_student] = {
            'Математика': [],
            'Русский язык': [],
            'Информатика': []
        }
        print('Новый ученик добавлен')
        print(f':{students}')
        print()
    elif command == 2:
        print('2. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 3:
        print('3. Средний бал ученика по предметам')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        for class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[student][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[student][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        print()
    elif command == 4:
        print('4. Все оценки ученика по всем предметам')
        student = input('Введите имя ученика: ')
        if student in students:
            # Цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 6:
        print('6. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 7:
        print('7. Оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            # Выводим Оценки ученика по предмету
            print(students_marks[student][class_])
            print()
        else:
            print('Этого ученика в списке нет')
    elif command == 8:
        print('8. Изменить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку которую хотите поменять: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # Удаляем оценку
            students_marks[student][class_].remove(mark)
            mark_1 = int(input('Введите новую оценку: '))
            # Добавляем новую оценку
            students_marks[student][class_].append(mark_1)
            # Выводим изменения
            print(f'Для {student} по предмету {class_} изменена оценка {mark} на оценку {mark_1}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
        print()
    elif command == 9:
        print('9. Удалить ученика')
        end_student = input('Введите имя ученика, которого хотите удалить: ')
        if end_student in students:
            # Удаляем ученика
            students.remove(end_student)
            print(f':{students}')
        else:
            print('Этого ученика в списке нет')
    elif command == 10:
        print('10. Выход из программы')
        break