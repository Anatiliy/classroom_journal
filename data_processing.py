import os
from new_data_structure import NewDataStructure as nds

class DataProcessing:

    def __init__(self, path: str, name='имя класса не задано'):
        self.name = name
        self.data = []
        self.path = path
        
        
    def __str__(self):
        return self.name

    def giveName(self, name: str):
        self.name = name

    def newEntry(self, student: str, subject: str):
        self.data.append(nds(student, subject))
        #self.data[-1] = nds(student, subject)

    def putScore(self,index, data: str):
        self.data[index].score.append(data)

    #def toStr(self):
        #return f"{self.name}*{';'.join(map(lambda item: item.conversToStr(), self.data))}"


    #def toData(self, text):
        #data = text.split('*')
        #self.name = data[0]
        #for item in data[1].split(';'):
            #self.data.append(nds())
            #self.data[-1].conversToNDS(item)

    # запись информации в файл
    def save(self):
        if self.data:
            data = [self.name].extend(list(map(lambda item: item.conversToStr(), self.data)))
            with open(self.path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(data)

        else:
            with open(self.path, 'w', encoding='utf-8') as output_file:
                output_file.write('')


    # считывание всей информации из файла
    def upload(self):
        with open(self.path, 'r', encoding='utf-8') as input_file:
            data = input_file.readlines()
        if data:
            for item in data:
                self.data.append(nds())
                self.data[-1].conversToNDS(item)
                

# перезапись файла информацией из переменной "data"
def overwrite(data):
    if data:
        with open('journal_list.csv', 'w', encoding='utf-8') as output_file:
            print(*data, sep='\n', file=output_file)
            #output_file.writelines(list(map(lambda item: ';'.join(item) + '\n', data)))

# считывание информации из файла
def read_data():
    if os.path.exists('journal_list.csv'):
        with open('journal_list.csv', 'r', encoding='utf-8') as input_file:
            data = list(map(lambda item: item.rstrip(), input_file.readlines()))
        return data
    else:
        return []


# поиск информации в файле по ключу "key" с последующей записью в переменную "result_data"
#def find(key):
    #with open('telephone_directory.csv', 'r', encoding='utf-8') as input_file:
        #data = input_file.readline()
        #result_data = []
        #while data != '':
            #data = data.strip().split(';')
            #if key.lower() in list(map(lambda item: item.lower(), data)):
                #result_data.append(data)
            #data = input_file.readline()
    #return result_data
    
