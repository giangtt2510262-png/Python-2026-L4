import math
from domains.student import Student
from domains.course import Course

def input_student(S):
    S.addstr("ID, Name, DoB (sep ';'): ")
    i, n, d = S.getstr().decode().split(';')
    return Student(i.strip(), n.strip(), d.strip())

def input_course(S):
    S.addstr("ID, Name, Credit (sep ';'): ")
    i, n, c = S.getstr().decode().split(';')
    return Course(i.strip(), n.strip(), c.strip())

def input_marks(S, A):
    S.addstr("Course ID: ")
    c = S.getstr().decode().strip()
    for s in A:
        S.addstr(f"Mark for {s.name}: ")
        s.marks[c] = math.floor(float(S.getstr().decode()) * 10) / 10
