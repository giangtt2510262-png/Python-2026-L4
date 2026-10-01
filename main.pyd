import curses
from input import input_student, input_course, input_marks
from output import show_gpa

def main(S):
    A, B = [], []
    while 1:
        S.clear()
        S.addstr("1.Add Student\n2.Add Course\n3.Input Marks\n4.Show GPA\n5.Exit\nOpt: ")
        curses.echo()
        k = S.getstr().decode().strip()
        if k == '1': A.append(input_student(S))
        elif k == '2': B.append(input_course(S))
        elif k == '3': input_marks(S, A)
        elif k == '4': show_gpa(S, A, B)
        elif k == '5': break

curses.wrapper(main)
