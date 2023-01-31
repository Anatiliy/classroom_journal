from data_processing import DataProcessing as dp
from view import View as vw
import data_processing as pdata


def main(journal_list=pdata.read_data()):
    
    value = vw.viewMenu(journal_list).lower()

    if value in journal_list:
        use_journal(value)

    elif value == '0':
        pdata.overwrite(journal_list)
        print('До свидания!')

    else:
        create_journal(value, journal_list)
        

       

def use_journal(name, journal_list):
    path = name + '_журнал.txt'
    class_journal = dp(path, name)
    class_journal.upload()
    value = vw.journalMenu(name).split('-')

    if value[0] == '1':
        vw.view_student(value[1].lower(), class_journal.data)
        use_journal(name, journal_list)

    elif value[0] == '2':
        use_subject(value[1], journal_list)
                
    
    else:
        main(journal_list)


def create_journal(name, journal_list):
    value = vw.newJournalMenu(name)
    if value == '1':
        journal_list.append(name)
        path = name + '_журнал.txt'
        class_journal = dp(path, name)
        class_journal.save()
        print(f'журнал "{name.upper()}" создан')
        main()
    else:
        main(journal_list)
    


def use_subject(name, class_journal):
    val = vw.view_subject(name.lower(), class_journal.data).split('-')
    match val:
        case str(val):
            class_journal.newEntry(val, name.lower())

        case str(val), '0':
            for item in class_journal.data:
                if item.subject == name and item.student == val:
                    class_journal.data.pop(class_journal.index(item))
                else:
                    print(f'Ученика с именем {val} нет в предмете {name}')
                    use_subject(name, class_journal)

        case str(val), '1'|'2'|'3'|'4'|'5' as score:
            for item in class_journal.data:
                if item.subject == name and item.student == val:
                    class_journal.putScore(class_journal.data.index(item), score)
                    print('Оценка выставлена.')
                    use_subject(name, class_journal)
                else:
                    print(f'Ученика с именем {val} нет в предмете {name}')
                    use_subject(name, class_journal)

        case _:
            create_journal(name, journal_list)

