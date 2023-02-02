class NewDataStructure:

    def __init__(self, student='student name', subject='subject name'):
        self.student = student
        self.subject = subject
        self.score = []
        

    def __str__(self):
        return f"|{self.student},{self.subject}:[{','.join(self.score)}]|"
    
    # присвоение новых значений атрибутам student и subject
    def rename(self, student='student name', subject='subject name'):
        self.student = student
        self.subject = subject
    
    # добавление данных в атрибут score
    def addat(self, data: str):
        self.score.append(data)
    
    # конвертация NewDataStructure в строку
    def conversToStr(self):
        return self.__str__()
    
    # конвертация строки в NewDataStructure
    def conversToNDS(self, data: str):
        data = data.strip('|').split(':')
        data[0] = data[0].split(',')
        self.student = data[0][0]
        self.subject = data[0][1]
        if data[1] == '[]':
            self.score = []
        else:
            self.score = data[1].strip('[]').split(',')

