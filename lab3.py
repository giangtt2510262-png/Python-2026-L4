import curses, math, numpy as np


class Course:

    def __init__(self, i, n, c):
        self.id, self.name, self.credit = i, n, int(c)


class Student:

    def __init__(self, i, n, d):
        self.id, self.name, self.dob = i, n, d
        self.marks, self.gpa = {}, 0.0

    def calc_gpa(self, C):
        m = [self.marks[c.id] for c in C if c.id in self.marks]
        w = [c.credit for c in C if c.id in self.marks]
        self.gpa = math.floor(np.average(m, weights=w) * 10) / 10 if w else 0.0


def main(S):
    A, B = [], []
    while 1:
        S.clear()
        S.addstr(
            "1.Add Student\n2.Add Course\n3.Input Marks\n4.Show GPA\n5.Exit\nOpt:"
        )
        curses.echo()
        k = S.getstr().decode().strip()
        if k == "1":
            S.addstr("ID, Name, DoB (sep ';'): ")
            i, n, d = S.getstr().decode().split(";")
            A.append(Student(i.strip(), n.strip(), d.strip()))
        elif k == "2":
            S.addstr("ID, Name, Credit (sep ';'): ")
            i, n, c = S.getstr().decode().split(";")
            B.append(Course(i.strip(), n.strip(), c.strip()))
        elif k == "3":
            S.addstr("Course ID: ")
            c = S.getstr().decode().strip()
            for s in A:
                S.addstr(f"Mark for {s.name}: ")
                s.marks[c] = math.floor(float(S.getstr().decode()) * 10) / 10
        elif k == "4":
            S.clear()
            for s in A:
                s.calc_gpa(B)
            A.sort(key=lambda x: x.gpa, reverse=True)
            for s in A:
                S.addstr(f"{s.id} | {s.name} | {s.dob} | GPA: {s.gpa}\n")
            curses.noecho()
            S.getch()
        elif k == "5":
            break


curses.wrapper(main)