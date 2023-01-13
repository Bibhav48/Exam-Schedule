from datetime import timedelta, datetime
from os import system
from time import sleep
from tkinter import *


class Exam:
    '''
    Parameters:
        name: str
        date: datetime
    '''

    Today = datetime.now()

    def __init__(self, name: str, date: datetime):
        self.name = name
        self.date = date

    def __month(self):
        month_number = self.date.month - 1
        months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]
        return months[month_number]

    def full_date(self):
        return f'{self.date.day}th {self.__month()} {self.date.year}'

    def __gt__(self, other):
        return self.date > other.date

    def __str__(self):
        return f'{self.name}:'+"\t"+f'{self.full_date()}'

    def create_ui(self):
        self.screen = Tk()
        self.screen.config(background='black')
        #self.screen.geometry( '1300x200')
        self.screen.resizable(0, 0)
        self.screen.title("EXAM COUNTDOWN")

    def display(self):
        Label(self.screen,text=self.name+":",font=('arial 15', 100), background="black", foreground="Cyan").pack(anchor='center')
        self.text = "{}"
        #self.text = self.name+":\n"+"{}"
        self.label = Label(self.screen, text=self.text.format(str(self.check_remaining(
        ))), font=('arial 15', 100), background="black", foreground="Orange")
        self.label.pack()
    


    def update(self):
        self.label.config(text=self.text.format(str(self.check_remaining())))
        self.screen.update()

    def completed(self):
        Exam.Today = datetime.now()
        return self.date < Exam.Today

    def check_remaining(self):
        Exam.Today = datetime.now()
        remaining = self.date - Exam.Today
        remaining = timedelta(seconds=int(remaining.total_seconds()))
        return remaining



ENGLISH_PAPER_1: Exam = Exam("English Paper 1", datetime(2022, 10, 19,12+2))
ENGLISH_PAPER_2: Exam = Exam("English Paper 2", datetime(2022, 10, 26,12+2))
MATHEMATICS_PURE: Exam = Exam("Pure Mathematic 1", datetime(2022, 10, 10,12+2))
MATHEMATICS_STATS: Exam = Exam("Statistics  1", datetime(2022, 10, 17,12+2))
COMPUTER_PAPER_1: Exam = Exam("Computer Paper 1", datetime(2022, 10, 13,10))
COMPUTER_PAPER_2: Exam = Exam("Computer Paper 2", datetime(2022, 10, 21,10))

Exams: list[Exam] = [ENGLISH_PAPER_1, ENGLISH_PAPER_2, MATHEMATICS_PURE,
                     MATHEMATICS_STATS, COMPUTER_PAPER_1, COMPUTER_PAPER_2]

Exams.sort(key=lambda x: x.date)

if __name__ == "__main__":

    next_exam = list(filter(lambda exam: not exam.completed(), Exams))[0]
    next_exam.create_ui()
    next_exam.display()

    #print('',*Exams, sep='\n',end='\n'*2)
    print("\nExams List:\n")
    error = False
    GUI, CLI = True, False
    while not error:
        for exam in Exams:
            if not exam.completed():
                if CLI:
                    text = str(exam)+"\t" + \
                        f"{exam.check_remaining()} days remaining"
                    print(text, end='\n')
                if GUI:
                    try:
                        next_exam.update()
                    except:
                        error = True
                        break
                # print('\b'*len(text),end='')
                # sleep(3)
        sleep(1)
        system('clear')

    Exams1: list[str] = sorted([str(i) for i in Exams])

    exam_names: list[str] = [exam.name for exam in Exams]
    exam_dates: list[str] = [exam.full_date() for exam in Exams]

    #print(*zip(exam_names,exam_dates), sep='\n',end='\n'*2)
