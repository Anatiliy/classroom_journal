class NewDataStructure:

    def __init__(self, student='student name', subject='subject name'):
        self.student = student
        self.subject = subject
        self.score = []
        

    def __str__(self):
        return f"|{self.student},{self.subject}:[{','.join(self.score)}]|"

    def rename(self, student='student name', subject='subject name'):
        self.student = student
        self.subject = subject

    def addat(self, data: str):
        self.score.append(data)

    def conversToStr(self):
        return self.__str__()

    def conversToNDS(self, data: str):
        data = data.strip('|').split(':')
        data[0] = data[0].split(',')
        self.student = data[0][0]
        self.subject = data[0][1]
        self.score = data[1].strip('[]').split(',')

