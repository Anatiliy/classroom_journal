
class View:

    def viewMenu():
        print('---------------------------------------------------------')
        print('                       ГЛАВНОЕ МЕНЮ                      ')
        print('---------------------------------------------------------')
        print('         Чтобы открыть журнал введите номер класса       ')
        print('           Чтобы создать новый журнал введите "1"        ')
        print('            Для выхода из программы введите "0"          ')
        print('---------------------------------------------------------')
        return input()


    def journalMenu(name):
        print('---------------------------------------------------------')
        print(f'                   ЖУРНАЛ {name} КЛАССА                  ')
        print('---------------------------------------------------------')
        print('Чтобы посмотреть успеваемость ученика введите имя ученика')
        print('      Чтобы открыть предмет введите название предмета    ')
        print('      Для выхода в ГЛАВНОЕ МЕНЮ введите любой символ     ')
        print('---------------------------------------------------------')
        return input()
