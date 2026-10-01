import curses

def show_gpa(S, A, B):
    S.clear()
    for s in A: s.calc_gpa(B)
    A.sort(key=lambda x: x.gpa, reverse=True)
    for s in A:
        S.addstr(f"{s.id} | {s.name} | {s.dob} | GPA: {s.gpa}\n")
    curses.noecho()
    S.getch()
