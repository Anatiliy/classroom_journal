from data_processing import DataProcessing as dp
from view import View as vw


def main():

    value = vw.viewMenu()

    match value:

        case '6А':
            journal(value)

        case '1':
            print('да')

        case '0':
            print('До свидания!')


def use_journal(name):
    value = vw.journalMenu(name)

    match value:

        case _:
            main()

