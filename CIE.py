from datetime import timedelta, datetime
from os import system
from time import sleep
from tkinter import *
from termcolor import cprint



class Exam:
    '''
    Parameters:
        name: str
        date: datetime
    '''

    Today = datetime.now()

    def __init__(self, name: str, date: datetime,time:timedelta):
        self.name = name
        self.date = date
        self.time = time

    def __month(self):
        month_number = self.date.month - 1
        months = ["January", "Feburary", "March", "April", "May", "June", "July",
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
        #self.screen.attributes('-zoomed', True)
        #self.screen.geometry( '1300x200')
        self.screen.resizable(0, 0)
        self.screen.title("EXAM COUNTDOWN")

    def display(self):
        Label(self.screen,text=self.name+":",font=('arial 15', 100), background="black", foreground="Cyan").pack(anchor='center')
        self.text = "{}"
        #self.text = self.name+":\n"+"{}"
        self.label = Label(self.screen, text=self.text.format(str(self.check_remaining(
        ))), font=('arial 15', 100), background="black", foreground=self.color)
        self.label.pack()
    


    def update(self):
        self.label.config(text=self.text.format(str(self.check_remaining())))
        self.screen.update()

    def completed(self):
        Exam.Today = datetime.now()
        return self.date < Exam.Today

    def check_remaining(self,other=None):
        Exam.Today = datetime.now()
        remaining = self.date - Exam.Today

        
        if remaining.days>10:
            self.color="cyan"
        elif remaining.days>7:
            self.color = "yellow"
        elif remaining.days>4:
            self.color = "blue"
        elif remaining.days>=0:
            self.color='red'
        else:
            self.color="green"

        if other:
            remaining = self.date - (other.time + other.date)

        remaining = timedelta(seconds=int(remaining.total_seconds()))

        if self.completed():
            return "EXAM COMPLETED"

        return remaining


ENGLISH_PAPER_1: Exam = Exam("English Paper 1", datetime(2022, 10, 19,12+2),timedelta(hours=2,minutes=15))
ENGLISH_PAPER_2: Exam = Exam("English Paper 2", datetime(2022, 10, 26,12+2),timedelta(hours=2))
MATHEMATICS_PURE: Exam = Exam("Pure Mathmatics 1", datetime(2022, 10, 10,12+2),timedelta(hours=1,minutes=50))
MATHEMATICS_STATS: Exam = Exam("Statstistics  1", datetime(2022, 10, 17,12+2), timedelta(hours=1,minutes=15))
COMPUTER_PAPER_1: Exam = Exam("Computer Paper 1", datetime(2022, 10, 13,10), timedelta(hours=1,minutes=30))
COMPUTER_PAPER_2: Exam = Exam("Computer Paper 2", datetime(2022, 10, 21,10), timedelta(hours=2))

Exams: list[Exam] = [ENGLISH_PAPER_1, ENGLISH_PAPER_2, MATHEMATICS_PURE,
                     MATHEMATICS_STATS, COMPUTER_PAPER_1, COMPUTER_PAPER_2]

Exams.sort(key=lambda x: x.date)
Completed = list(filter(lambda exam: exam.completed(), Exams))
Exams = list(filter(lambda exam: not exam.completed(), Exams))



              ###MAIN###

if __name__ == "__main__":
    GUI, CLI = False, True
    if GUI:
        next_exam = Exams[0]
        next_exam.create_ui()
        next_exam.display()

    #print('',*Exams, sep='\n',end='\n'*2)
    print("\nExams List:\n")
    error = False
    while not error:
        for index,exam in enumerate(Completed+Exams):

            if index >= len(Completed):
                check = exam.check_remaining(prev_exam)
                msg = f"after {check} days of\t {prev_exam.name}"
            else:
                check = exam.check_remaining()
                if isinstance(check,str):
                    msg = check
                else:
                    msg = f"{check} days remaining"
                

            if CLI:
                text = str(exam)+"\t" + msg
                cprint(text,color=exam.color, end='\n')
            if GUI:
                try:
                    next_exam.update()
                except:
                    error = True
                    break
                # print('\b'*len(text),end='')
                # sleep(3)
            prev_exam=exam
        sleep(1)
        system('clear')

    Exams1: list[str] = sorted([str(i) for i in Exams])

    exam_names: list[str] = [exam.name for exam in Exams]
    exam_dates: list[str] = [exam.full_date() for exam in Exams]

    #print(*zip(exam_names,exam_dates), sep='\n',end='\n'*2)
