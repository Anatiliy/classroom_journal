import os
from new_data_structure import NewDataStructure as nds

class DataProcessing:

    def __init__(self, path: str, name='имя класса не задано'):
        self.name = name
        self.data = []
        self.path = path
        
        
    def __str__(self):
        return self.name
    
    # присвоение атрибуту name нового значения
    def giveName(self, name: str):
        self.name = name
    
    # добавление иформации в атрибут data
    def newEntry(self, student: str, subject: str):
        self.data.append(nds(student, subject))
        
    # добавление оценки ученику
    def putScore(self,index, data: str):
        self.data[index].score.append(data)

    # сохранение экземпляра класса в файл
    def save(self):
        if self.data:
            data = [self.name] + list(map(lambda item: item.conversToStr(), self.data))
            with open(self.path, 'w', encoding='utf-8') as output_file:
                print(*data, sep='\n', file=output_file)

        else:
            with open(self.path, 'w', encoding='utf-8') as output_file:
                output_file.write('')

    # считывание всей информации из файла
    def upload(self):
        with open(self.path, 'r', encoding='utf-8') as input_file:
            data = list(map(lambda item: item.rstrip(), input_file.readlines()))
        if data:
            self.name = data.pop(0)
            for item in data:
                self.data.append(nds())
                self.data[-1].conversToNDS(item)

# перезапись файла информацией из переменной "data"
def overwrite(data):
    if data:
        with open('journal_list.csv', 'w', encoding='utf-8') as output_file:
            print(*data, sep='\n', file=output_file)
            
# считывание информации из файла
def read_data():
    if os.path.exists('journal_list.csv'):
        with open('journal_list.csv', 'r', encoding='utf-8') as input_file:
            data = list(map(lambda item: item.rstrip(), input_file.readlines()))
        return data
    else:
        return []

