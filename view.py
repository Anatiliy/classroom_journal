
class View:
    
    # вывод на экран главного меню
    def viewMenu(journal_list):
        print('-------------------------------------------------------------------------')
        print('                              ГЛАВНОЕ МЕНЮ')
        print('-------------------------------------------------------------------------')
        print(' Чтобы открыть журнал или создать новый введите номер класса, используя  ')
        print('                        цифры и латинские буквы')
        print('                  Для выхода из программы введите "0"')
        print('-------------------------------------------------------------------------')
        print('                            Доступные журналы:')
        if journal_list:
            print(*journal_list)
        else:
            print('                          Доступных журналов нет')
        print('-------------------------------------------------------------------------')
        return input('                                ')

    # вывод на экран меню журнала
    def journalMenu(name):
        print('-------------------------------------------------------------------------')
        print(f'                          ЖУРНАЛ "{name.upper()}" КЛАССА')
        print('-------------------------------------------------------------------------')
        print('        Чтобы посмотреть успеваемость ученика введите "имя ученика-1"')
        print(' Чтобы открыть предмет или содать новую запись введите "название предмета-2" ')
        print('              Для выхода в ГЛАВНОЕ МЕНЮ введите любой символ')
        print('-------------------------------------------------------------------------')
        return input('                             ')

    # вывод на экран меню создания нового журнала
    def newJournalMenu(name):
        print('-------------------------------------------------------------------------')
        print(f'                      ЖУРНАЛ "{name.upper()}" НЕ СУЩЕСТВУЕТ')
        print('-------------------------------------------------------------------------')
        print(f'              Чтобы создать журнал с именем "{name.upper()}" введите "1"')
        print('              Для выхода в ГЛАВНОЕ МЕНЮ введите любой символ')
        print('-------------------------------------------------------------------------')
        return input('                                ')
    
    # вывод на экран информации по ученику
    def view_student(name, data):
        if data:
            print('-------------------------------------------------------------------------')
            print(f'                                 {name}')
            print('-------------------------------------------------------------------------')
            for item in data:
                if name == item.student:
                    print(item.subject, *item.score)
        else:
            print('-------------------------------------------------------------------------')
            print('                             Журнал пуст')
            print('-------------------------------------------------------------------------')
    
    # вывод на экран информации по предмету    
    def view_subject(name, data):
        if data:
            print('-------------------------------------------------------------------------')
            print(f'                              {name}')
            print('-------------------------------------------------------------------------')
            for item in data:
                if name == item.subject:
                    print(item.student, *item.score) 
        else:
            print('-------------------------------------------------------------------------')
            print(f'                              {name}')
            print('-------------------------------------------------------------------------')
            print('                             Журнал пуст')
            print('-------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------')
        print('            Чтобы вписать ученика в предмет введите "имя ученика-9"')
        print('         Чтобы удалить ученика из предмета введите "имя ученика-0"')
        print('        Чтобы поставить ученику оценку введите "имя ученика-оценка"')
        print('              Для выхода в МЕНЮ журнала введите любой символ')
        print('-------------------------------------------------------------------------')
        return input('                             ')
    
    # вывод на экран сообщения massage
    def viewMassage(massage):
        print(massage)
