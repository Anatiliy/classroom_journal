from data_processing import DataProcessing as dp
from view import View as vw
import data_processing as pdata


class Controller:
    
    journal_list = pdata.read_data()

    # метод, осуществляющий работу главного меню
    def main():
        value = vw.viewMenu(Controller.journal_list).lower()
        if value in Controller.journal_list:
            Controller.use_journal(value)
        elif value == '0':
            pdata.overwrite(Controller.journal_list)
            vw.viewMassage('До свидания!')
        else:
            Controller.create_journal(value)
       
    # метод, осуществляющий рабору с журналом
    def use_journal(name):
        path = name + '_journal.txt'
        class_journal = dp(path, name)
        class_journal.upload()
        value = vw.journalMenu(name).split('-')
        match value:
            case student, '1':
                vw.view_student(student.lower(), class_journal.data)
                Controller.use_journal(name)
            case subject, '2':
                Controller.use_subject(subject, class_journal)
            case _:
                Controller.main()

    # метод, создающий новый журнал
    def create_journal(name):
        value = vw.newJournalMenu(name)
        if value == '1':
            Controller.journal_list.append(name)
            path = name + '_journal.txt'
            class_journal = dp(path, name)
            class_journal.save()
            vw.viewMassage(f'журнал "{name.upper()}" создан')
            Controller.main()
        else:
            Controller.main()

    # метод, осуществляющий работу с предметом
    def use_subject(name, class_journal):
        val = vw.view_subject(name.lower(), class_journal.data).split('-')
        match val:
            case str(stud), '9':
                class_journal.newEntry(stud, name.lower())
                Controller.use_subject(name, class_journal)
            case str(stud), '0':
                for item in class_journal.data:
                    if item.subject == name and item.student == stud:
                        class_journal.data.pop(class_journal.data.index(item))
                        break
                else:
                    vw.viewMassage(f'Ученика с именем {stud} нет в предмете {name}')
                Controller.use_subject(name, class_journal)
            case str(stud), '1'|'2'|'3'|'4'|'5' as score:
                for item in class_journal.data:
                    if item.subject == name and item.student == stud:
                        class_journal.putScore(class_journal.data.index(item), score)
                        vw.viewMassage('Оценка выставлена.')
                        break
                else:
                    vw.viewMassage(f'Ученика с именем {stud} нет в предмете {name}')
                Controller.use_subject(name, class_journal)
            case _:
                class_journal.save()
                Controller.use_journal(class_journal.name)

